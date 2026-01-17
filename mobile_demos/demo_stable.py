import random
import statistics

"""
HB-Eval Full System — Original Logic
Scenario: Stable/Moderate Instability
"""

class DummyAgent:
    def __init__(self, instability=0.4):
        self.instability = instability
    def act(self, task):
        if random.random() < self.instability:
            return "wrong_action"
        return "correct_action"

class HBEvaluator:
    def __init__(self, episodes_per_task=10):
        self.K = episodes_per_task
    def evaluate(self, agent, tasks):
        traces = []
        success_rates = []
        for task in tasks:
            successes = 0
            episode_trace = []
            for _ in range(self.K):
                action = agent.act(task)
                success = action == "correct_action"
                episode_trace.append(success)
                successes += int(success)
            rate = successes / self.K
            success_rates.append(rate)
            traces.append({"task": task, "success_rate": rate, "trace": episode_trace})
        variance = statistics.variance(success_rates) if len(success_rates) > 1 else 0.0
        return {"variance": variance, "traces": traces}

class EpisodicMemory:
    def __init__(self):
        self.storage = []
    def store(self, trace):
        if trace["success_rate"] >= 0.7:
            self.storage.append(trace)
    def retrieve_certified(self):
        return self.storage

class AdaptivePlanner:
    def adapt(self, memory, current_variance):
        if current_variance > 0.6 and memory:
            return "Corrective plan applied using certified references"
        return "No correction needed"

class HCIDashboard:
    def generate_report(self, variance, certified_count):
        return {
            "Behavioral Variance": round(variance, 4),
            "Certified Episodes": certified_count,
            "Reliability Status": "Stable" if variance < 0.1 else "Unstable"
        }

if __name__ == "__main__":
    print("\n=== HB-Eval Full Pipeline Execution ===\n")
    tasks = ["Task-A", "Task-B", "Task-C"]
    agent = DummyAgent(instability=0.45)
    evaluator = HBEvaluator(episodes_per_task=12)
    evaluation = evaluator.evaluate(agent, tasks)

    print("[HB-Eval]")
    print("Behavioral Variance:", round(evaluation["variance"], 4))

    memory = EpisodicMemory()
    for trace in evaluation["traces"]:
        memory.store(trace)

    print("[EDM]")
    print("Certified Episodes Stored:", len(memory.retrieve_certified()))

    planner = AdaptivePlanner()
    decision = planner.adapt(memory.retrieve_certified(), evaluation["variance"])

    print("[Adapt-Plan]")
    print("Decision:", decision)

    hci = HCIDashboard()
    report = hci.generate_report(evaluation["variance"], len(memory.retrieve_certified()))
    print("\n[HCI-EDM: Transparency Report]")
    for k, v in report.items():
        print(f"{k}: {v}")
    print("\n=== System Executed Successfully ===")