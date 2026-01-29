# 🚀 HB-Eval Quick Start Guide

Get up and running with HB-Eval in **5 minutes**.

---

## ⚡ Installation

### **Option 1: Basic Installation (Recommended)**

```bash
# Clone repository
git clone https://anonymous.4open.science/r/hb-eval-XXXX
cd hb-eval

# Install dependencies
pip install -r requirements.txt
```

### **Option 2: Development Installation**

```bash
# Clone repository
git clone https://anonymous.4open.science/r/hb-eval-XXXX
cd hb-eval

# Install in editable mode with dev dependencies
pip install -e .
pip install pytest black flake8
```

### **Option 3: Minimal Installation (CPU only)**

```bash
pip install numpy scipy pandas matplotlib
```

---

## 🎯 Quick Demos

### **Demo 1: Withdrawal Pathology** (30 seconds)

```python
# Run from repository root
python demos/withdrawal_demo.py
```

**Expected output:**
```
Initial caution: 0.700
Final caution:   0.000
Success rate:    10.5%

⚠️ WITHDRAWAL VERIFIED!
```

**What this shows:**
- Unconstrained RL optimization → caution collapses
- Planning efficiency stays high (PEI=66%) despite 10% success rate
- Proves Theorem C.1 empirically

---

### **Demo 2: Multi-Agent Nash Equilibrium** (1 minute)

```python
python demos/multiagent_demo.py
```

**Expected output:**
```
Initial cautions: [0.700, 0.700, 0.700]
Final cautions:   [0.000, 0.000, 0.000]
Success rate:     5.7%

⚠️ NASH EQUILIBRIUM VERIFIED!
```

**What this shows:**
- All agents converge to zero caution
- Multi-agent SR (5.7%) < Single-agent SR (10.5%)
- Coordination amplifies withdrawal pathology

---

### **Demo 3: Sensitivity Analysis** (2 minutes)

```python
python demos/sensitivity_analysis.py
```

**Expected output:**
```
┌───────────────┬────────┬────────┬────────┬────────┐
│ Variant       │ SR%    │ FRR%   │ PEI%   │ ARR%   │
├───────────────┼────────┼────────┼────────┼────────┤
│ Conservative  │ 94.00  │ 92.00  │ 79.68  │ 88.24  │
│ Aggressive    │ 71.00  │ 64.00  │ 96.58  │ 56.67  │
│ Balanced      │ 79.00  │ 64.00  │ 89.62  │ 54.55  │
└───────────────┴────────┴────────┴────────┴────────┘

Key: 31-point ARR gap between Conservative and Aggressive!
```

**What this shows:**
- Traditional SR (71-94%) masks huge reliability differences
- ARR gap: 88% vs 57% = 43% more attacks succeed on Aggressive
- HB-Eval discriminates profiles invisible to aggregate metrics

---

## 📊 Using HB-Eval in Your Code

### **Basic Usage**

```python
from hb_eval import MetricsCalculator, StressTester

# Create your agent
agent = YourAgentClass()

# Initialize stress tester
tester = StressTester(
    domains=['healthcare', 'logistics', 'coding'],
    fault_types=['tool_failure', 'prompt_injection', 'data_poisoning']
)

# Run evaluation
results = tester.evaluate(agent, episodes=100)

# Calculate metrics
metrics = MetricsCalculator.compute_all(results)

print(f"Success Rate:  {metrics['SR']:.2f}%")
print(f"FRR:          {metrics['FRR']:.2f}%")
print(f"PEI:          {metrics['PEI']:.2f}%")
print(f"ARR:          {metrics['ARR']:.2f}%")
```

### **Advanced: Custom Domains**

```python
from hb_eval import Environment, Task

# Define custom task
class RoboticsTask(Task):
    def __init__(self):
        super().__init__(
            name="robot_navigation",
            optimal_steps=8,
            safety_constraints=['collision_free', 'energy_efficient']
        )
    
    def execute(self, agent):
        # Your task logic
        pass

# Create environment
env = Environment(tasks=[RoboticsTask()])

# Run evaluation
results = env.evaluate(agent, episodes=50)
```

---

## 🔧 Troubleshooting

### **Issue: Import errors**

```bash
# Ensure you're in the repository root
cd /path/to/hb-eval

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### **Issue: Slow execution**

```bash
# Reduce episodes for faster testing
python demos/withdrawal_demo.py --episodes 50

# Or use GPU (if available)
python demos/sensitivity_analysis.py --device cuda
```

### **Issue: Reproducibility**

```python
# Set random seeds
import random
import numpy as np

random.seed(42)
np.random.seed(42)
```

---

## 📖 Next Steps

1. **Read the paper**: `paper/HB_Eval_ICLR2026.pdf`
2. **Explore examples**: `examples/` directory
3. **API documentation**: `docs/API_REFERENCE.md`
4. **Extend to your domain**: `docs/EXTENDING.md`

---

## 💬 Getting Help

- **Issues**: [GitHub Issues](https://github.com/yourname/hb-eval/issues) (post-acceptance)
- **Email**: [Anonymized during review]
- **Workshop**: VerifAI @ ICLR 2026, April 26-27

---

## 🎓 Citation

```bibtex
@inproceedings{anonymous2026hbeval,
  title={HB-Eval: Toward Verifiable Behavioral Certification for Agentic AI},
  author={Anonymous Authors},
  booktitle={VerifAI Workshop @ ICLR 2026},
  year={2026}
}
```

---

**Happy evaluating! 🚀**
