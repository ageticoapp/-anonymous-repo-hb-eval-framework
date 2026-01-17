import random
import statistics

print("\n=== HB-Eval Dual-Trigger Adaptation Scenario ===\n")

class UnstableAgent:
    def run_episode(self):
        return random.random() > 0.7

class HBEval:
    def evaluate(self, agent, episodes=20):
        results = [agent.run_episode() for _ in range(episodes)]
        sr = sum(results) / len(results)
        var = statistics.pvariance([int(r) for r in results])
        return {"success_rate": sr, "variance": var}

class EDM:
    def __init__(self, success_threshold=0.6):
        self.threshold = success_threshold
        self.memory = []
    def store(self, trace):
        if trace["success_rate"] >= self.threshold:
            self.memory.append(trace)
            return True
        return False

class AdaptPlan:
    def __init__(self, var_threshold=0.05):
        self.var_threshold = var_threshold
    def decide(self, trace, edm):
        print("\n[Adapt-Plan]")
        if trace["variance"] > self.var_threshold:
            if edm.memory:
                print("Mode: Reference-Based Correction ✔")
                return "CORRECT_WITH_MEMORY"
            else:
                print("Mode: ⚠ Risk-Mitigation (No Certified Memory)")
                return "RISK_MITIGATION"
        print("Mode: Stable")
        return "STABLE"

if __name__ == "__main__":
    agent = UnstableAgent()
    hb = HBEval()
    trace = hb.evaluate(agent)

    print("[HB-Eval]")
    print(f"Success Rate: {trace['success_rate']:.2f}")
    print(f"Variance: {trace['variance']:.4f}")

    edm = EDM()
    stored = edm.store(trace)
    print("\n[EDM]")
    print("Memory Stored ✔" if stored else "No Certified Memory ✖")

    adapt = AdaptPlan()
    decision = adapt.decide(trace, edm)

    print("\n[HCI-EDM]")
    print(f"Final Decision: {decision}")