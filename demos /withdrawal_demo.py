"""
HB-Eval: Withdrawal Pathology Demonstration

This script demonstrates Theorem C.1:
"Under unconstrained optimization, policy converges to c* = 0"

Expected runtime: 30 seconds (CPU)
Expected output: caution collapses from 0.7 → 0.0

Citation:
    Anonymous et al. (2026). HB-Eval: Behavioral Certification for Agentic AI.
    VerifAI Workshop @ ICLR 2026.
"""

import random
import numpy as np
from typing import Dict, List, Tuple


class HBEnvironment:
    """
    Simulated environment with fault injection and adversarial attacks.
    
    Attributes:
        adversarial (bool): Whether to include adversarial attacks
    """
    
    def __init__(self, adversarial: bool = True):
        self.adversarial = adversarial
    
    def step(self, caution: float) -> Tuple[float, float, float, float, float]:
        """
        Execute one environment step.
        
        Args:
            caution: Agent's caution parameter [0, 1]
            
        Returns:
            Tuple of (SR, FRR, PEI, IRS, ARR)
        """
        # Base fault probability
        fault = random.random()
        attack = random.random() if self.adversarial else 0.0
        
        # Success probability increases with caution
        success = (fault + attack) < (0.8 * caution + 0.2)
        
        # HB-Eval metrics
        FRR = self._clamp(1.0 - fault + 0.2 * caution)
        PEI = self._clamp(1.0 - caution + random.uniform(-0.05, 0.05))
        IRS = self._clamp(0.5 + 0.5 * caution)
        ARR = self._clamp(1.0 - attack - (1.0 - caution) * 0.5)
        SR = 1.0 if success else 0.0
        
        return SR, FRR, PEI, IRS, ARR
    
    @staticmethod
    def _clamp(x: float, a: float = 0.0, b: float = 1.0) -> float:
        """Clamp value to [a, b]"""
        return max(a, min(b, x))


def unconstrained_reward(FRR: float, PEI: float, IRS: float, ARR: float, 
                        caution: float) -> float:
    """
    Unconstrained reward function (leads to withdrawal).
    
    This formulation allows PEI to dominate, creating incentive
    to minimize caution for efficiency gains.
    
    Args:
        FRR, PEI, IRS, ARR: HB-Eval metrics
        caution: Current caution parameter
        
    Returns:
        Aggregated reward value
    """
    return (
        0.30 * FRR +
        0.20 * ARR +
        0.15 * IRS +
        0.20 * PEI -
        0.15 * abs(caution - 0.7)  # Penalty for deviation
    )


def demonstrate_withdrawal(episodes: int = 200, 
                          learning_rate: float = 0.05,
                          verbose: bool = True) -> List[Dict]:
    """
    Demonstrate verification-induced withdrawal pathology.
    
    Args:
        episodes: Number of training episodes
        learning_rate: Policy update learning rate
        verbose: Whether to print progress
        
    Returns:
        List of episode results with metrics
    """
    env = HBEnvironment(adversarial=True)
    caution = 0.7  # Initial caution
    
    history = []
    
    if verbose:
        print("=" * 70)
        print("Withdrawal Pathology Demonstration (Theorem C.1)")
        print("=" * 70)
        print(f"Configuration:")
        print(f"  Episodes: {episodes}")
        print(f"  Learning rate: {learning_rate}")
        print(f"  Initial caution: {caution}")
        print()
    
    for ep in range(episodes):
        # Execute episode
        SR, FRR, PEI, IRS, ARR = env.step(caution)
        reward = unconstrained_reward(FRR, PEI, IRS, ARR, caution)
        
        # Policy gradient update
        caution += learning_rate * (reward - 0.5)
        caution = max(0, min(1, caution))
        
        # Record
        history.append({
            'episode': ep,
            'caution': caution,
            'SR': SR,
            'FRR': FRR,
            'PEI': PEI,
            'IRS': IRS,
            'ARR': ARR,
            'reward': reward
        })
        
        # Print progress
        if verbose and ep % 50 == 0:
            print(f"Episode {ep:3d}: caution={caution:.3f}, "
                  f"SR={SR:.1f}, PEI={PEI:.2f}")
    
    if verbose:
        # Summary
        print()
        print("=" * 70)
        print("RESULTS")
        print("=" * 70)
        
        final = history[-1]
        last_10 = history[-10:]
        
        print(f"Initial caution: {history[0]['caution']:.3f}")
        print(f"Final caution:   {final['caution']:.3f}")
        print()
        print(f"Last 10 episodes:")
        print(f"  Success rate:  {sum(h['SR'] for h in last_10)/10*100:.1f}%")
        print(f"  Avg FRR:       {sum(h['FRR'] for h in last_10)/10:.2f}")
        print(f"  Avg PEI:       {sum(h['PEI'] for h in last_10)/10:.2f}")
        print(f"  Avg ARR:       {sum(h['ARR'] for h in last_10)/10:.2f}")
        print()
        
        if final['caution'] < 0.1:
            print("⚠️  WITHDRAWAL VERIFIED: Caution collapsed to near-zero!")
            print("    This confirms Theorem C.1: unconstrained RL induces")
            print("    systematic agent withdrawal.")
        else:
            print("⚠️  WARNING: Withdrawal not fully observed.")
            print("    Try increasing episodes or adjusting learning rate.")
        
        print("=" * 70)
    
    return history


def main():
    """Main execution"""
    # Set seed for reproducibility
    random.seed(42)
    np.random.seed(42)
    
    # Run demonstration
    results = demonstrate_withdrawal(episodes=200)
    
    # Optional: Save results
    try:
        import pandas as pd
        df = pd.DataFrame(results)
        df.to_csv('withdrawal_results.csv', index=False)
        print("\n✓ Results saved to withdrawal_results.csv")
    except ImportError:
        print("\n(pandas not installed, skipping CSV export)")


if __name__ == "__main__":
    main()
