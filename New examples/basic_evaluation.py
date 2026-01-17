"""
Basic Evaluation Example
-------------------------
A minimal implementation demonstrating how to use the HB-Eval core 
to assess a custom agent's reliability.
"""

import random
from hb_eval.evaluator import HBEvaluator

class MyCustomAgent:
    """A simulated agent with 75% success probability."""
    def act(self, task_id):
        # Simulating agent stochasticity
        return "success" if random.random() > 0.25 else "failure"

def main():
    # 1. Initialize tasks and agent
    tasks = ["navigation_01", "form_filling_02", "data_retrieval_03"]
    agent = MyCustomAgent()

    # 2. Configure Evaluator (K=10 episodes per task)
    evaluator = HBEvaluator(episodes_per_task=10)

    print(f"🚀 Starting HB-Eval on {len(tasks)} tasks...")
    
    # 3. Run evaluation
    results = evaluator.evaluate(agent, tasks)

    # 4. Print Summary Report
    print("\n" + "="*30)
    print("HB-EVAL SUMMARY REPORT")
    print("="*30)
    print(f"Mean Success Rate: {results['mean_success']:.2f}")
    print(f"Behavioral Variance: {results['variance']:.4f}")
    
    status = "RELIABLE" if results['variance'] < 0.05 else "UNSTABLE"
    print(f"Reliability Status: {status}")
    print("="*30)

if __name__ == "__main__":
    main()