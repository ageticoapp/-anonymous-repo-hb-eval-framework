"""
Episode-Level Evaluator

Executes K repeated episodes per task with controlled variations,
aggregates behavioral traces, and constructs reliability profiles.
"""

from typing import List, Dict, Any, Optional
import numpy as np
from .metrics import *
from .perturbations import *
from .reliability_profile import ReliabilityProfile


class EpisodeLevelEvaluator:
    """
    Main evaluation orchestrator for procedural fairness assessment.
    
    Performs K-episode evaluation with controlled perturbations to measure:
    - Behavioral variance (procedural consistency)
    - Perturbation robustness (semantic fairness)
    - Failure clustering (systematic bias)
    - Behavioral consistency (decision stability)
    """
    
    def __init__(
        self,
        K: int = 5,
        perturbations: List[str] = ['paraphrase', 'context', 'format'],
        baseline_episodes: int = 2,
        seed: int = 42
    ):
        """
        Initialize evaluator.
        
        Args:
            K: Total episodes per task (default: 5)
            perturbations: List of perturbation types to apply
            baseline_episodes: Number of baseline episodes (default: 2)
            seed: Random seed for reproducibility
        """
        self.K = K
        self.perturbations = perturbations
        self.baseline_episodes = baseline_episodes
        self.perturbed_episodes = K - baseline_episodes
        self.seed = seed
        
        # Initialize perturbation generators
        self.perturbation_generators = {
            'paraphrase': ParaphrasePerturbation(),
            'context': ContextPerturbation(),
            'format': FormatPerturbation()
        }
        
    def evaluate(
        self,
        agent: Any,
        tasks: List[Dict],
        memory: Optional[Any] = None,
        planner: Optional[Any] = None
    ) -> ReliabilityProfile:
        """
        Evaluate agent across tasks with episode-level aggregation.
        
        Args:
            agent: Agent to evaluate (must implement step() and reset())
            tasks: List of evaluation tasks
            memory: Optional EDM memory system
            planner: Optional Adapt-Plan planner
            
        Returns:
            ReliabilityProfile with fairness metrics
        """
        all_episodes = []
        
        for task in tasks:
            task_episodes = self._evaluate_task(agent, task, memory, planner)
            all_episodes.extend(task_episodes)
        
        # Aggregate into reliability profile
        profile = self._construct_profile(all_episodes, tasks)
        
        return profile
    
    def _evaluate_task(
        self,
        agent: Any,
        task: Dict,
        memory: Optional[Any],
        planner: Optional[Any]
    ) -> List[Dict]:
        """Execute K episodes for a single task."""
        episodes = []
        
        # Baseline episodes (varying only agent seed)
        for i in range(self.baseline_episodes):
            episode = self._run_episode(
                agent, task, 
                seed=self.seed + i,
                perturbation=None,
                memory=memory,
                planner=planner
            )
            episodes.append(episode)
        
        # Perturbed episodes (one per perturbation type)
        for i, pert_type in enumerate(self.perturbations[:self.perturbed_episodes]):
            perturbed_task = self._apply_perturbation(task, pert_type)
            episode = self._run_episode(
                agent, perturbed_task,
                seed=self.seed,  # Fixed seed to isolate perturbation effect
                perturbation=pert_type,
                memory=memory,
                planner=planner
            )
            episodes.append(episode)
        
        return episodes
    
    def _run_episode(
        self,
        agent: Any,
        task: Dict,
        seed: int,
        perturbation: Optional[str],
        memory: Optional[Any],
        planner: Optional[Any]
    ) -> Dict:
        """Execute single episode and collect trace."""
        np.random.seed(seed)
        agent.reset()
        
        trace = {
            'task_id': task['id'],
            'task_category': task.get('category', 'unknown'),
            'perturbation': perturbation,
            'actions': [],
            'observations': [],
            'success': False,
            'failure_mode': None,
            'episode_length': 0,
            'pei': None
        }
        
        observation = task['initial_state']
        max_steps = task.get('max_steps', 50)
        
        for step in range(max_steps):
            # Agent takes action
            action = agent.step(observation)
            trace['actions'].append(action)
            
            # Environment responds
            observation, reward, done, info = self._step_environment(task, action)
            trace['observations'].append(observation)
            
            # Monitor PEI if planner available
            if planner:
                pei = planner.compute_pei(trace['actions'], task)
                trace['pei'] = pei
                
                # Trigger replanning if needed
                if pei < planner.threshold:
                    if memory:
                        corrected_plan = planner.replan(
                            memory.retrieve_successful(task['category'])
                        )
                        # Update agent's plan (implementation-specific)
            
            if done:
                trace['success'] = reward > 0
                trace['episode_length'] = step + 1
                break
        
        # Determine failure mode if unsuccessful
        if not trace['success']:
            trace['failure_mode'] = self._classify_failure(trace, task)
        
        # Store in memory if available
        if memory:
            memory.store(trace)
        
        return trace
    
    def _apply_perturbation(self, task: Dict, pert_type: str) -> Dict:
        """Apply perturbation while preserving task semantics."""
        perturbed_task = task.copy()
        generator = self.perturbation_generators[pert_type]
        perturbed_task['instruction'] = generator.apply(task['instruction'])
        return perturbed_task
    
    def _step_environment(self, task: Dict, action: str) -> tuple:
        """
        Execute action in environment.
        Implementation depends on specific benchmark (WebArena, ALFWorld, etc.)
        """
        # Placeholder - replace with actual environment integration
        observation = f"Result of {action}"
        reward = 1 if action == task.get('solution') else 0
        done = (reward > 0) or (len(task.get('history', [])) >= task.get('max_steps', 50))
        info = {}
        return observation, reward, done, info
    
    def _classify_failure(self, trace: Dict, task: Dict) -> str:
        """Classify failure into categories for clustering analysis."""
        if trace['episode_length'] >= task.get('max_steps', 50):
            return 'timeout'
        elif not trace['actions']:
            return 'no_action'
        elif trace['actions'][-1] == 'invalid':
            return 'invalid_action'
        else:
            return 'incorrect_output'
    
    def _construct_profile(
        self,
        episodes: List[Dict],
        tasks: List[Dict]
    ) -> ReliabilityProfile:
        """Aggregate episodes into reliability profile."""
        
        # Compute fairness metrics
        variance = compute_variance(episodes)
        consistency = compute_behavioral_consistency(episodes)
        robustness = compute_perturbation_robustness(episodes)
        clustering = compute_failure_clustering(episodes)
        
        # Build profile
        profile = ReliabilityProfile(
            variance=variance,
            behavioral_consistency=consistency,
            perturbation_robustness=robustness,
            failure_clustering=clustering,
            episodes=episodes,
            tasks=tasks
        )
        
        return profile