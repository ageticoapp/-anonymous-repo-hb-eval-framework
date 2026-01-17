# 📊 Metrics Guide

This document provides the formal definitions and interpretations of the metrics used in the **HB-Eval** framework to assess agentic fairness and reliability.

## 1. Behavioral Variance ($\sigma^2$)
This is the core metric for **Procedural Fairness**. It measures the stochasticity of the agent's success across repeated trials.

- **Formula**: $\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}$
- **Interpretation**: 
    - **Low Variance (< 0.05)**: High procedural fairness; the agent treats scenarios consistently.
    - **High Variance (> 0.15)**: Low procedural fairness; identical requests receive arbitrary outcomes.

## 2. Planning Efficiency Index (PEI)
Calculated by the **Adapt-Plan** module, PEI measures how direct the agent's reasoning path is compared to an optimal reference.

- **Formula**: $PEI = \frac{\text{Optimal Steps}}{\text{Actual Steps}}$
- **Interpretation**: A low PEI indicates "looping" behavior or redundant reasoning, often a precursor to catastrophic failure.

## 3. Failure Resilience Rate (FRR)
Measures the effectiveness of the **EDM (Episodic Decision Memory)** in helping the agent recover from errors.

- **Formula**: $FRR = \frac{\text{Successful Recoveries via Memory}}{\text{Total Encountered Failures}}$
- **Interpretation**: High FRR proves that the agent is successfully "learning" from certified episodic traces stored in memory.

## 4. Traceability Index (TI)
A metric for accountability within the **HCI-EDM** layer, measuring the percentage of agent actions that are fully logged with an audit trail.

- **Goal**: $TI \rightarrow 1.0$ for high-stakes deployment (e.g., healthcare or legal agents).