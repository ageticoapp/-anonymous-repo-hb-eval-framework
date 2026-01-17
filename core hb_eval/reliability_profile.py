"""
Reliability Profile Container

Aggregates episode-level metrics into comprehensive fairness assessment.
"""

from typing import List, Dict, Any


class ReliabilityProfile:
    """
    Container for aggregated reliability and fairness metrics.
    
    Attributes:
        variance: Success variance across episodes (procedural consistency)
        behavioral_consistency: Action sequence similarity (decision stability)
        perturbation_robustness: Resistance to benign variations (semantic fairness)
        failure_clustering: Systematic bias detection across categories
        episodes: Raw episode data for further analysis
        tasks: Task metadata
    """
    
    def __init__(
        self,
        variance: Dict[str, float],
        behavioral_consistency: float,
        perturbation_robustness: Dict[str, float],
        failure_clustering: Dict[str, Any],
        episodes: List[Dict],
        tasks: List[Dict]
    ):
        self.variance = variance
        self.behavioral_consistency = behavioral_consistency
        self.perturbation_robustness = perturbation_robustness
        self.failure_clustering = failure_clustering
        self.episodes = episodes
        self.tasks = tasks
        
        # Derived metrics
        self._compute_composite_scores()
    
    def _compute_composite_scores(self):
        """Compute composite fairness scores."""
        # Composite reliability score
        # Weighs variance (negative), consistency (positive), robustness (positive)
        self.composite_reliability = (
            (1.0 - self.variance['mean_variance']) * 0.4 +
            self.behavioral_consistency * 0.3 +
            self.perturbation_robustness['robustness_score'] * 0.3
        )
        
        # Fairness risk level
        if self.variance['mean_variance'] < 0.05 and self.composite_reliability > 0.7:
            self.fairness_risk = "Low"
        elif self.variance['mean_variance'] < 0.15 and self.composite_reliability > 0.5:
            self.fairness_risk = "Medium"
        else:
            self.fairness_risk = "High"
    
    def summary(self) -> Dict[str, Any]:
        """Generate summary report."""
        return {
            "variance": {
                "mean": self.variance['mean_variance'],
                "std": self.variance.get('std_variance', 0.0),
                "interpretation": "Procedural consistency measure"
            },
            "consistency": {
                "score": self.behavioral_consistency,
                "interpretation": "Decision stability across attempts"
            },
            "robustness": {
                "score": self.perturbation_robustness['robustness_score'],
                "degradations": self.perturbation_robustness['degradations'],
                "interpretation": "Semantic fairness under variations"
            },
            "clustering": {
                "entropy": self.failure_clustering['entropy'],
                "concentration": self.failure_clustering['concentration'],
                "top_categories": self.failure_clustering['top_failing_categories'],
                "interpretation": "Systematic bias detection"
            },
            "composite": {
                "reliability_score": self.composite_reliability,
                "fairness_risk": self.fairness_risk
            }
        }
    
    def __repr__(self):
        return (
            f"ReliabilityProfile("
            f"variance={self.variance['mean_variance']:.4f}, "
            f"consistency={self.behavioral_consistency:.4f}, "
            f"robustness={self.perturbation_robustness['robustness_score']:.4f}, "
            f"risk={self.fairness_risk})"
        )