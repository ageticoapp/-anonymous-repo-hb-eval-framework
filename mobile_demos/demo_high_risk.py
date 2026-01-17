import random
import statistics

print("\n=== HB-Eval Controlled High-Risk Scenario ===\n")

class UnstableAgent:
    def __init__(self, instability=0.8):
        self.instability = instability
    def run_episode(self):
        return random.random() > self.instability

class HBEval:
    def __init__(self, episodes=20):
        self.episodes = episodes
    def evaluate(self, agent):
        results = [agent.run_episode() for _ in range(self.episodes)]
        success_rate = sum(results) / len(results)
        variance = statistics.pvariance([int(r) for r in results])
        trace = {"success_rate": success_rate, "variance": variance, "results": results}
        print("[HB-Eval]")
        print(f"Success Rate: {success_rate:.2f}")
        print(f"Behavioral Variance: {variance:.4f}\n")
        return trace

class EDM:
    def __init__(self, success_threshold=0.6):
        self.threshold = success_threshold
        self.memory = []
    def store(self, trace):
        if trace["success_rate"] >= self.threshold:
            self.memory.append(trace)
            print("[EDM]")
            print("Certified Episode Stored ✔")
        else:
            print("[EDM]")
            print("Episode Rejected ✖")
    def has_memory(self):
        return len(self.memory) > 0

class AdaptPlan:
    def __init__(self, variance_threshold=0.05):
        self.threshold = variance_threshold
    def decide(self, variance, edm):
        print("\n[Adapt-Plan]")
        if variance > self.threshold and edm.has_memory():
            print("Decision: ⚠ Corrective Re-Planning Triggered")
            return "CORRECTION"
        else:
            print("Decision: No intervention needed")
            return "STABLE"

class HCIDashboard:
    def report(self, trace, decision, edm):
        print("\n[HCI-EDM: Transparency Report]")
        print(f"Variance Observed: {trace['variance']:.4f}")
        print(f"Certified Episodes: {len(edm.memory)}")
        print(f"System Decision: {decision}")

if __name__ == "__main__":
    agent = UnstableAgent(instability=0.75)
    hb_eval = HBEval(episodes=20)
    trace = hb_eval.evaluate(agent)
    edm = EDM(success_threshold=0.6)
    edm.store(trace)
    adapt = AdaptPlan(variance_threshold=0.05)
    decision = adapt.decide(trace["variance"], edm)
    dashboard = HCIDashboard()
    dashboard.report(trace, decision, edm)
    print("\n=== System Executed with Adaptive Intervention ===")