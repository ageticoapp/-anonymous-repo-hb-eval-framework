# 📱 HB-Eval Mobile Demos (Original Logic)

This directory contains the exact scripts used to generate the validation results for the HB-Eval framework. These scripts require no external libraries and run on any standard Python 3 environment.

## 🚀 Execution Guide

1. **Scenario 1: Full Pipeline (Stable)**
   - Run: `python demo_stable.py`
   - Focus: Demonstrates the basic flow (HB-Eval -> EDM -> Adapt-Plan -> HCI).

2. **Scenario 2: Controlled High-Risk**
   - Run: `python demo_high_risk.py`
   - Focus: Shows how the system rejects unstable agents and avoids blind intervention.

3. **Scenario 3: Dual-Trigger Adaptation**
   - Run: `python demo_adaptive.py`
   - Focus: Shows the "Risk-Mitigation" logic when no certified memory is available.

---

## 📊 Expected Numerical Outputs
Based on initial validation:
- **Stable Case**: Variance ~0.0162
- **High-Risk Case**: Variance ~0.2275 | Decision: STABLE (No memory found)
- **Adaptive Case**: Variance ~0.2475 | Mode: RISK_MITIGATION