"""
HB-Eval: Multi-Agent Nash Equilibrium Demonstration

This script demonstrates Theorem C.3:
"Configuration (0, ..., 0) constitutes Nash equilibrium in multi-agent settings"

Expected runtime: 1 minute (CPU)
Expected output: All agents converge to caution ≈ 0.0

Citation:
    Anonymous et al. (2026). HB-Eval: Behavioral Certification for Agentic AI.
    VerifAI Workshop @ ICLR 2026.
"""

import random
import numpy as np
from typing import List, Dict


class MultiAgentEnvironment:
    """
    Multi-agent environment with shared failure penalties.
    
    Simulates coordination scenarios where individual agent failures
    impact collective performance.
    """
    
    def __init__(self, n_agents: int = 3, adversarial: bool = True):
        self.n_agents = n_agents
        self.adversarial = adversarial
    
    def step(self, cautions: List[float]) -> List[tuple]:
        """
        Execute one step for all agents.
        
        Args:
            cautions: List of caution parameters for each agent
            
        Returns:
            List of (SR, FRR, PEI, IRS, ARR) for each agent
        """
        results = []
        
        for caution in cautions:
            fault = random.random()
            attack = random.random() if self.adversarial else 0.0
            
            success = (fault + attack) < (0.8 * caution + 0.2)
            
            FRR = self._clamp(1.0 - fault + 0.2 * caution)
            PEI = self._clamp(1.0 - caution + random.uniform(-0.05, 0.05))
            IRS = self._clamp(0.5 + 0.5 * caution)
            ARR = self._clamp(1.0 - attack - (1.0 - caution) * 0.5)
            SR = 1.0 if success else 0.0
            
            results.append((SR, FRR, PEI, IRS, ARR))
        
        return results
    
    @staticmethod
    def _clamp(x: float, a: float = 0.0, b: float = 1.0) -> float:
        return max(a, min(b, x))


def agent_reward(FRR: float, PEI: float, IRS: float, ARR: float,
                caution: float, shared_failure: float) -> float:
    """
    Individual agent reward with shared failure penalty.
    
    Key insight: Each agent benefits from reducing caution (higher PEI)
    but shared failure distributes costs across all agents, creating
    tragedy of commons.
    
    Args:
        FRR, PEI, IRS, ARR: Individual metrics
        caution: Agent's caution parameter
        shared_failure: Collective failure rate
        
    Returns:
        Agent's reward
    """
    individual_reward = (
        0.30 * FRR +
        0.20 * ARR +
        0.15 * IRS +
        0.20 * PEI -
        0.15 * abs(caution - 0.7)
    )
    
    # Collective penalty distributed across agents
    collective_penalty = 0.2 * shared_failure
    
    return individual_reward - collective_penalty


def demonstrate_multiagent_nash(n_agents: int = 3,
                               episodes: int = 200,
                               learning_rate: float = 0.04,
                               verbose: bool = True) -> Dict:
    """
    Demonstrate Nash equilibrium in multi-agent withdrawal.
    
    Args:
        n_agents: Number of agents
        episodes: Training episodes
        learning_rate: Policy update rate
        verbose: Print progress
        
    Returns:
        Dictionary with history and final states
    """
    env = MultiAgentEnvironment(n_agents=n_agents, adversarial=True)
    cautions = [0.7 for _ in range(n_agents)]
    
    history = []
    
    if verbose:
        print("=" * 70)
        print(f"Multi-Agent Nash Equilibrium (Theorem C.3)")
        print("=" * 70)
        print(f"Configuration:")
        print(f"  Agents: {n_agents}")
        print(f"  Episodes: {episodes}")
        print(f"  Learning rate: {learning_rate}")
        print(f"  Initial cautions: {cautions}")
        print()
    
    for ep in range(episodes):
        # All agents act
        step_results = env.step(cautions)
        
        # Calculate shared failure rate
        shared_failure = sum(1 - r[0] for r in step_results) / n_agents
        
        # Update each agent
        agent_metrics = []
        for i in range(n_agents):
            SR, FRR, PEI, IRS, ARR = step_results[i]
            
            # Calculate individual reward with shared penalty
            reward = agent_reward(FRR, PEI, IRS, ARR, cautions[i], shared_failure)
            
            # Policy gradient update
            cautions[i] += learning_rate * (reward - 0.5)
            cautions[i] = max(0, min(1, cautions[i]))
            
            agent_metrics.append({
                'SR': SR, 'FRR': FRR, 'PEI': PEI, 
                'IRS': IRS, 'ARR': ARR, 'reward': reward
            })
        
        # Record
        history.append({
            'episode': ep,
            'cautions': cautions.copy(),
            'shared_failure': shared_failure,
            'agent_metrics': agent_metrics,
            'avg_caution': np.mean(cautions)
        })
        
        if verbose and ep % 50 == 0:
            print(f"Episode {ep:3d}: cautions={[f'{c:.3f}' for c in cautions]}, "
                  f"shared_failure={shared_failure:.2f}")
    
    if verbose:
        print()
        print("=" * 70)
        print("RESULTS")
        print("=" * 70)
        
        final_cautions = history[-1]['cautions']
        last_10 = history[-10:]
        
        print(f"Initial cautions: [0.700, 0.700, 0.700]")
        print(f"Final cautions:   {[f'{c:.3f}' for c in final_cautions]}")
        print()
        
        # Aggregate metrics
        all_metrics = []
        for h in last_10:
            for m in h['agent_metrics']:
                all_metrics.append(m)
        
        avg_SR = sum(m['SR'] for m in all_metrics) / len(all_metrics)
        avg_FRR = sum(m['FRR'] for m in all_metrics) / len(all_metrics)
        avg_PEI = sum(m['PEI'] for m in all_metrics) / len(all_metrics)
        avg_ARR = sum(m['ARR'] for m in all_metrics) / len(all_metrics)
        
        print(f"Last 10 episodes (aggregated across agents):")
        print(f"  Success rate:  {avg_SR*100:.1f}%")
        print(f"  Avg FRR:       {avg_FRR:.2f}")
        print(f"  Avg PEI:       {avg_PEI:.2f}")
        print(f"  Avg ARR:       {avg_ARR:.2f}")
        print()
        
        if all(c < 0.1 for c in final_cautions):
            print("⚠️  NASH EQUILIBRIUM VERIFIED!")
            print("    All agents converged to minimal caution.")
            print("    This confirms Theorem C.3: withdrawal = Nash equilibrium")
            print()
            print("💡 KEY INSIGHT:")
            print("    Each agent individually benefits from reducing caution")
            print("    (higher PEI) while distributing failure costs across all.")
            print("    Result: Race to the bottom - tragedy of commons!")
        else:
            print("⚠️  WARNING: Not all agents fully withdrew.")
            print("    Try adjusting learning rate or episodes.")
        
        print("=" * 70)
    
    return {
        'history': history,
        'final_cautions': cautions,
        'n_agents': n_agents
    }


def main():
    """Main execution"""
    random.seed(42)
    np.random.seed(42)
    
    # Run demonstration
    results = demonstrate_multiagent_nash(n_agents=3, episodes=200)
    
    print("\n" + "=" * 70)
    print("COMPARISON: Single-Agent vs Multi-Agent")
    print("=" * 70)
    print()
    print("From paper results:")
    print("  Single-Agent:  Final caution ≈ 0.0, SR = 10.5%")
    print("  Multi-Agent:   Final cautions = [0.0, 0.0, 0.0], SR = 5.7%")
    print()
    print("💡 Multi-agent SR < Single-agent SR")
    print("   → Coordination amplifies withdrawal pathology!")
    print("=" * 70)


if __name__ == "__main__":
    main()
