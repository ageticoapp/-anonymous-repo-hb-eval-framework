# 🏁 Getting Started with HB-Eval

Welcome to the **HB-Eval** documentation. This guide will help you set up the environment and conduct your first behavioral certification for an AI agent.

## 1. Installation

HB-Eval is designed to be lightweight and portable. It requires **Python 3.8+** and has no mandatory external dependencies for its core logic.

```bash
# Clone the repository
git clone [https://github.com/](https://github.com/)[anonymous]/hb-eval-framework.git
cd hb-eval-framework

# (Optional) Install pytest for running the validation suite
pip install pytest
2. Core Concept: Episodic AggregationUnlike standard benchmarks that run a task once, HB-Eval uses Episodic Aggregation. Each task is executed $K$ times (default $K=10$) to observe the distribution of outcomes. This allows us to measure:Reliability: How often does the agent succeed?Procedural Fairness: How consistent is the agent's behavior under identical constraints?3. Basic WorkflowTo evaluate an agent, you only need three steps:Define your Agent: Your agent should have a method that accepts a task and returns a success/failure signal.Initialize Evaluator: Set your desired number of episodes ($K$).Run & Analyze: Execute the evaluation and review the generated Reliability Profile.4. Running the DemosIf you are using a mobile environment (like Pydroid3), we recommend starting with the mobile_demos/ directory, which contains self-contained scripts for rapid testing.

python mobile_demos/demo_stable.py