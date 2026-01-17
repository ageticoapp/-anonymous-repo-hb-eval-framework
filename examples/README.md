
# 📖 Examples Guide

This directory provides practical, ready-to-use scripts to help you integrate your AI agents with the **HB-Eval** framework. These examples bridge the gap between theoretical research and operational implementation.

---

## 📂 Included Examples

### 1. `basic_evaluation.py`

**Goal:** The fastest way to see HB-Eval in action.

* Uses a **Mock Agent** to simulate success/failure.
* Demonstrates how to initialize the `HBEvaluator`.
* Outputs a summary of **Success Rate** and **Behavioral Variance**.

### 2. `fairness_audit.py` (Experimental)

**Goal:** Identifying systematic bias across task categories.

* Groups tasks into types (e.g., Navigation vs. Form Filling).
* Detects if an agent is "unfairly" failing in specific domains despite a high overall average.

---

## 🛠️ Execution Instructions

To ensure all internal references work correctly, run the examples from the **root directory** of the project using the module flag:

```bash
# Run the basic evaluation example
python -m examples.basic_evaluation

```

---

## 🧩 Integration Pattern

To evaluate your own agent (e.g., GPT-4, Claude, or a custom LLM-chain), follow this pattern used in the examples:

1. **Wrap your agent**: Ensure your agent has an `.act()` or `.step()` method.
2. **Define Tasks**: Create a list of task descriptions or IDs.
3. **Run Evaluator**: Pass the agent and tasks to `HBEvaluator(episodes_per_task=K)`.
4. **Analyze**: Use the returned dictionary to inspect `variance` and `consistency`.

---

## 📊 Understanding the Output

When you run the examples, pay attention to the **Reliability Status**:

| Variance () | Status | Action |
| --- | --- | --- |
| **< 0.05** | ✅ **STABLE** | Safe for deployment. |
| **0.05 - 0.15** | ⚠️ **VOLATILE** | Requires monitoring via `Adapt-Plan`. |
| **> 0.15** | 🚫 **UNSTABLE** | High risk of **Procedural Unfairness**. |

---

## 📱 Mobile Compatibility

If you are running these on **Pydroid3** or a mobile terminal, these examples are fully compatible as they rely on the zero-dependency core logic.

-