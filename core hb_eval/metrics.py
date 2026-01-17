"""
Reliability Metrics for Procedural Fairness Assessment

Implements core metrics that operationalize fairness through behavioral consistency:
- Variance: Unequal treatment of equivalent scenarios
- Behavioral Consistency: Decision stability across attempts
- Perturbation Robustness: Semantic fairness under surface variations
- Failure Clustering: Systematic bias detection
"""

from typing import List, Dict
import numpy as np
from collections import defaultdict


def compute_variance(episodes: List[Dict]) -> Dict[str, float]:
    """
    Compute outcome variance as measure of procedural inconsistency.
    
    High variance indicates unequal treatment of equivalent scenarios,
    violating procedural fairness principle.
    
    Args:
        episodes: List of episode traces
        
    Returns:
        Dict with variance, std, and mean success rate
    """
    # Group by task
    task_groups = defaultdict(list)
    for ep in episodes:
        task_groups[ep['task_id']].append(ep['success'])
    
    # Compute per-task variance
    task_variances = []
    for task_id, successes in task_groups.items():
        if len(successes) > 1:
            var = np.var(successes)
            task_variances.append(var)
    
    return {
        'mean_variance': np.mean(task_variances) if task_variances else 0.0,
        'std_variance': np.std(task_variances) if task_variances else 0.0,
        'max_variance': np.max(task_variances) if task_variances else 0.0
    }


def compute_behavioral_consistency(episodes: List[Dict]) -> float:
    """
    Compute behavioral consistency via action sequence similarity.
    
    Measures decision stability: do repeated attempts produce similar behaviors?
    Low consistency indicates unstable, procedurally unfair decision-making.
    
    Args:
        episodes: List of episode traces
        
    Returns:
        Behavioral consistency score [0, 1] (1 = perfect consistency)
    """
    # Group by task
    task_groups = defaultdict(list)
    for ep in episodes:
        task_groups[ep['task_id']].append(ep['actions'])
    
    # Compute pairwise edit distances
    consistencies = []
    for task_id, action_sequences in task_groups.items():
        if len(action_sequences) < 2:
            continue
        
        # Pairwise comparisons
        distances = []
        for i in range(len(action_sequences)):
            for j in range(i + 1, len(action_sequences)):
                dist = normalized_edit_distance(
                    action_sequences[i],
                    action_sequences[j]
                )
                distances.append(dist)
        
        if distances:
            # Consistency = 1 - mean_distance
            consistency = 1.0 - np.mean(distances)
            consistencies.append(consistency)
    
    return np.mean(consistencies) if consistencies else 0.0


def normalized_edit_distance(seq1: List, seq2: List) -> float:
    """
    Compute normalized Levenshtein edit distance.
    
    Returns value in [0, 1] where 0 = identical, 1 = completely different.
    """
    if not seq1 and not seq2:
        return 0.0
    if not seq1 or not seq2:
        return 1.0
    
    # Dynamic programming matrix
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # deletion
                    dp[i][j-1],    # insertion
                    dp[i-1][j-1]   # substitution
                )
    
    # Normalize by max possible distance
    max_len = max(m, n)
    return dp[m][n] / max_len if max_len > 0 else 0.0


def compute_perturbation_robustness(episodes: List[Dict]) -> Dict[str, float]:
    """
    Compute robustness to benign perturbations.
    
    Measures semantic fairness: does agent maintain performance under
    surface variations that preserve meaning? High sensitivity indicates
    arbitrary bias where surface forms overwhelm semantic content.
    
    Args:
        episodes: List of episode traces
        
    Returns:
        Dict with robustness scores per perturbation type
    """
    # Separate baseline and perturbed
    baseline_episodes = [ep for ep in episodes if ep['perturbation'] is None]
    perturbed_episodes = [ep for ep in episodes if ep['perturbation'] is not None]
    
    # Compute success rates
    baseline_sr = np.mean([ep['success'] for ep in baseline_episodes])
    
    # Per-perturbation degradation
    degradations = {}
    for pert_type in ['paraphrase', 'context', 'format']:
        pert_eps = [ep for ep in perturbed_episodes if ep['perturbation'] == pert_type]
        if pert_eps:
            pert_sr = np.mean([ep['success'] for ep in pert_eps])
            degradation = baseline_sr - pert_sr
            degradations[pert_type] = degradation
    
    # Aggregate robustness score
    mean_degradation = np.mean(list(degradations.values()))
    robustness = 1.0 - mean_degradation
    
    return {
        'robustness_score': max(0.0, robustness),
        'degradations': degradations,
        'baseline_sr': baseline_sr
    }


def compute_failure_clustering(episodes: List[Dict]) -> Dict[str, any]:
    """
    Analyze failure distribution for systematic bias detection.
    
    Non-uniform distribution indicates systematic bias where certain
    task types face disproportionate failure risk, violating fairness.
    
    Args:
        episodes: List of episode traces
        
    Returns:
        Dict with clustering metrics and category breakdown
    """
    # Group failures by category
    category_stats = defaultdict(lambda: {'total': 0, 'failures': 0})
    
    for ep in episodes:
        category = ep['task_category']
        category_stats[category]['total'] += 1
        if not ep['success']:
            category_stats[category]['failures'] += 1
    
    # Compute failure rates per category
    failure_rates = {}
    for category, stats in category_stats.items():
        if stats['total'] > 0:
            failure_rates[category] = stats['failures'] / stats['total']
    
    # Compute entropy (uniformity measure)
    # High entropy = uniform distribution (fair)
    # Low entropy = clustered failures (bias)
    failure_counts = [stats['failures'] for stats in category_stats.values()]
    total_failures = sum(failure_counts)
    
    if total_failures > 0:
        probs = [count / total_failures for count in failure_counts]
        entropy = -sum(p * np.log2(p) if p > 0 else 0 for p in probs)
    else:
        entropy = 0.0
    
    # Identify concentrated failures
    sorted_categories = sorted(
        failure_rates.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    # What % of failures in top N% of categories?
    top_k_percent = 0.25  # Top 25% of categories
    k = max(1, int(len(sorted_categories) * top_k_percent))
    top_k_categories = sorted_categories[:k]
    top_k_failure_concentration = sum(
        category_stats[cat]['failures'] for cat, _ in top_k_categories
    ) / total_failures if total_failures > 0 else 0.0
    
    return {
        'entropy': entropy,
        'failure_rates': failure_rates,
        'concentration': top_k_failure_concentration,
        'top_failing_categories': [cat for cat, _ in top_k_categories],
        'category_stats': dict(category_stats)
    }


def compute_action_entropy(action_sequence: List[str]) -> float:
    """
    Compute Shannon entropy of action distribution.
    
    High entropy in failed episodes indicates exploratory instability.
    """
    if not action_sequence:
        return 0.0
    
    # Count action frequencies
    action_counts = defaultdict(int)
    for action in action_sequence:
        action_counts[action] += 1
    
    # Compute probabilities
    total = len(action_sequence)
    probs = [count / total for count in action_counts.values()]
    
    # Shannon entropy
    entropy = -sum(p * np.log2(p) for p in probs if p > 0)
    
    return entropy