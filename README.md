# HB-Eval: Procedural Fairness Evaluation for Agentic AI

<p align="left">
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-yellow.svg" alt="Python"></a>
  <img src="https://img.shields.io/badge/Status-Anonymous%20Review-orange" alt="Status">
  <img src="https://img.shields.io/badge/ICLR%202026-AFAA%20Workshop-blue" alt="ICLR">
  <img src="https://img.shields.io/badge/Mobile-Ready-green" alt="Mobile">
</p>

---

## 🎯 **Overview**

**Anonymous submission for ICLR 2026 Workshop on Algorithmic Fairness across Alignment procedures and Agentic systems (AFAA).**

HB-Eval establishes that **reliability is a fundamental prerequisite for algorithmic fairness** in autonomous agents. An agent with high behavioral variance or unpredictable failures under identical constraints is inherently *procedurally unfair*.

### **The Problem**
```
Agent A: 70% success, σ=0.08  → Consistent (procedurally fair)
Agent B: 70% success, σ=0.14  → Volatile (procedurally unfair)

Same average, drastically different fairness.
```

### **Our Solution**
Episode-level evaluation (K=5 repeated attempts) reveals:
- **Variance**: 1.75× difference across agents → unequal treatment
- **Systematic Bias**: 68% failures in 23% of categories → targeted unfairness  
- **Perturbation Brittleness**: 34% degradation → arbitrary sensitivity

**Integrated system achieves 37% variance reduction and 18% robustness improvement.**

---

## 🚀 **Quick Start**

### **Option 1: Full Framework (Recommended)**
```bash
git clone https://github.com/[anonymous]/hb-eval-framework.git
cd hb-eval-framework
pip install -r requirements.txt

# Run evaluation
python examples/basic_evaluation.py
```

### **Option 2: Zero-Dependency Mobile Demo** 📱
```bash
# Works on phones (Pydroid3), embedded systems, anywhere!
cd mobile_demos
python demo_stable.py        # Scenario 1: Stable agent
python demo_high_risk.py     # Scenario 2: High-risk detection
python demo_adaptive.py      # Scenario 3: Adaptive mitigation
```

**No numpy, no pandas, no ML libraries required.** Pure Python for maximum accessibility.

---

## 📊 **Key Results**

| Metric | Finding | Implication |
|--------|---------|-------------|
| **Behavioral Variance** | 8-14% (1.75× difference) | Unequal treatment of equivalent scenarios |
| **Systematic Bias** | 68% failures in 23% categories | Concentrated unfairness amenable to mitigation |
| **Perturbation Sensitivity** | 12-34% degradation | Arbitrary surface-form dependencies |
| **System Impact** | 37% variance ↓, 18% robustness ↑ | Quantifiable procedural fairness improvement |

---

## 🏗️ **Architecture**

```
┌──────────────────────────────────────────────────────┐
│  HB-Eval: Detection (variance, clustering, robustness)│
└────────────────┬─────────────────────────────────────┘
                 ↓ Violations detected
┌──────────────────────────────────────────────────────┐
│  Adapt-Plan: Correction (PEI monitoring, replanning) │
└────────────────┬─────────────────────────────────────┘
                 ↓ References retrieved
┌──────────────────────────────────────────────────────┐
│  EDM: Certification (episode storage, FRR, TI=0.98)  │
└────────────────┬─────────────────────────────────────┘
                 ↓ Evidence extracted
┌──────────────────────────────────────────────────────┐
│  HCI-EDM: Accountability (explanations, audit UI)    │
└──────────────────────────────────────────────────────┘
```

---

## 📱 **Mobile Demos - Zero Dependencies**

Three progressive scenarios demonstrating core concepts:

### **Demo 1: Stable Agent Detection**
```python
python mobile_demos/demo_stable.py
```
**Output:**
```
Variance: 0.0162
Status: Stable ✓
Decision: No intervention needed
```
→ System correctly identifies procedurally fair behavior

### **Demo 2: High-Risk Detection**
```python
python mobile_demos/demo_high_risk.py
```
**Output:**
```
Success Rate: 0.35
Variance: 0.2275
Status: High risk detected ⚠️
Certified Memory: None
```
→ System detects procedural unfairness but lacks correction data

### **Demo 3: Adaptive Mitigation**
```python
python mobile_demos/demo_adaptive.py
```
**Output:**
```
Variance: 0.2475
Decision: RISK_MITIGATION
Action: Prevent unfair deployment ✓
```
→ System enters safe mode, blocking procedurally unfair agent

**These demos validate framework logic on any device—phones, IoT, embedded systems—proving implementation-agnostic reliability assessment.**

---

## 🔬 **Core Metrics**

| Metric | Formula | Fairness Dimension |
|--------|---------|-------------------|
| **Variance (σ²)** | `Var(successes)` | Procedural consistency |
| **Behavioral Consistency (BC)** | `1 - EditDist(sequences)` | Decision stability |
| **Perturbation Robustness (PR)** | `1 - mean(degradation)` | Semantic fairness |
| **Failure Clustering (FC)** | Entropy of error distribution | Systematic bias |
| **Planning Efficiency (PEI)** | `GoalAchievement / Cost` | Resource fairness |
| **Failure Resilience (FRR)** | `Recoveries / Failures` | Learning capacity |
| **Traceability Index (TI)** | `Logged / Total` | Audit compliance |

---

## 📂 **Repository Structure**

```
hb-eval-framework/
├── hb_eval/              # Core evaluation framework
│   ├── evaluator.py      # Episode-level evaluation
│   ├── metrics.py        # Fairness metrics
│   └── perturbations.py  # Semantic-preserving variations
│
├── mobile_demos/         # 🔥 Zero-dependency demos
│   ├── demo_stable.py
│   ├── demo_high_risk.py
│   └── demo_adaptive.py
│
├── examples/             # Integration examples
│   ├── basic_evaluation.py
│   └── integrated_system.py
│
└── docs/                 # Documentation
    ├── getting_started.md
    └── metrics_guide.md
```

---

## 💡 **Why This Matters**

### **For Research**
- First framework linking reliability to procedural fairness
- Episode-level methodology reveals hidden unfairness
- Reproducible across environments (desktop → mobile)

### **For Deployment**
- Pre-deployment fairness assessment
- Real-time monitoring and correction
- Audit-ready compliance (TI=0.98)

### **For Education**
- Zero-dependency demos for teaching
- Progressive complexity (3 scenarios)
- Accessible on any device

---

## 🧪 **Reproducing Paper Results**

```bash
# Table 1: Main results (WebArena + ALFWorld)
python examples/reproduce_table1.py

# Figure 1: Reliability gap visualization
python examples/reproduce_figure1.py

# End-to-end integrated system demo
python examples/integrated_system.py
```

---

## 🎯 **Use Cases**

### **1. Fairness Assessment**
```python
from hb_eval import EpisodeLevelEvaluator

evaluator = EpisodeLevelEvaluator(K=5)
profile = evaluator.evaluate(agent, tasks)

if profile.variance > 0.12:
    print("⚠️ Procedural unfairness detected")
```

### **2. Real-Time Monitoring**
```python
from adapt_plan import AdaptivePlanner

planner = AdaptivePlanner(pei_threshold=0.5)
if planner.compute_pei(trajectory) < 0.5:
    corrected_plan = planner.replan(memory.retrieve())
```

### **3. Audit Compliance**
```python
from edm import EpisodicMemory

memory = EpisodicMemory()
memory.store(episode)
assert memory.traceability_index >= 0.98  # Regulatory requirement
```

---

## 📖 **Documentation**

- **[Getting Started](docs/getting_started.md)** - Installation and first steps
- **[Metrics Guide](docs/metrics_guide.md)** - Detailed metric explanations
- **[Mobile Demos](mobile_demos/README.md)** - Zero-dependency scenarios

---

## 🤝 **Contributing**

This repository is under anonymous review for ICLR 2026 AFAA Workshop.

**During review period:** Please direct questions through conference submission system.

**After acceptance:** Full contribution guidelines will be published.

---

## 📄 **Citation**

```bibtex
@inproceedings{anonymous2026hbeval,
  title={HB-Eval: Episode-Level Reliability Evaluation for Agentic AI Systems},
  author={Anonymous Authors},
  booktitle={ICLR 2026 Workshop on AFAA},
  year={2026},
  note={Under review}
}
```

---

## 🛡️ **License**

Apache License 2.0

---

## ⭐ **Highlights**

- ✅ **Mobile-Ready**: Runs on phones with zero dependencies
- ✅ **Fairness-First**: Reliability operationalized as procedural fairness
- ✅ **Integrated System**: Detection → Correction → Certification → Accountability
- ✅ **Reproducible**: Identical results across platforms
- ✅ **Accessible**: Progressive demos from simple to advanced

---

<p align="center">
  <b>Anonymous Submission for ICLR 2026 AFAA Workshop</b><br>
  <i>"Reliability is not orthogonal to fairness—it is constitutive of it."</i>
</p>

---

**Last Updated:** January 2026  
**Status:** Under Anonymous Review# HB-Eval: Procedural Fairness Evaluation for Agentic AI Systems

<p align="left">
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-yellow.svg" alt="Python"></a>
  <img src="https://img.shields.io/badge/Status-Anonymous%20Review-orange" alt="Status">
  <img src="https://img.shields.io/badge/ICLR%202026-AFAA%20Workshop-blue" alt="ICLR">
</p>

---

## 🎯 **Project Overview**

This repository contains the **anonymous implementation** of the **HB-Eval framework** and its integrated components, submitted to the **ICLR 2026 Workshop on Algorithmic Fairness across Alignment procedures and Agentic systems (AFAA)**.

**Framework Components:**
1. **HB-Eval** - Episode-level behavioral certification for procedural fairness assessment
2. **Adapt-Plan** - Real-time efficiency-aware planning with alignment correction
3. **EDM (Evaluation-Driven Memory)** - Certified episodic memory with audit trails
4. **HCI-EDM** - Performance-grounded interpretability for human accountability

**Core Contribution:**  
We establish that **reliability is a fundamental prerequisite for algorithmic fairness** in autonomous agentic systems. An agent exhibiting high behavioral variance or unpredictable failures under identical constraints is inherently *procedurally unfair*, as it treats equivalent scenarios inconsistently.

> **⚠️ Anonymous Submission Notice**  
> This repository is maintained for double-blind peer review. All identifying information has been removed.  
> **Full release with complete documentation will follow upon acceptance.**

---

## 🔬 **What is HB-Eval?**

Current agent benchmarks test systems once per task and report aggregate success rates. But **averages hide unfairness**.

Consider two AI agents, both succeeding 70% of the time:
- **Agent A**: Low variance (σ=0.08) → consistent experience for all users
- **Agent B**: High variance (σ=0.14) → some users get instant solutions, others suffer through failures

**Same average, drastically different procedural fairness.**

HB-Eval reveals this hidden unfairness by:
- Testing agents across **K=5 repeated episodes** with controlled variations
- Applying **realistic perturbations** (paraphrasing, formatting, context changes)
- Measuring **variance, robustness, clustering, and consistency**
- Detecting **systematic bias** where failures concentrate in specific task categories

---

## 📊 **Key Findings**

Evaluation of three architectures (ReAct, Reflexion, Tree-of-Thought) on WebArena and ALFWorld reveals:

| Metric | Finding | Fairness Implication |
|--------|---------|---------------------|
| **Behavioral Variance** | Differs **1.75×** (σ: 0.08–0.14) | Unequal treatment of equivalent scenarios |
| **Systematic Bias** | **68%** of failures in **23%** of categories | Non-uniform risk distribution |
| **Perturbation Sensitivity** | Up to **34%** degradation | Arbitrary surface-form dependencies |
| **Behavioral Instability** | **3.2×** higher divergence in failures | Unpredictable decision processes |

**With Integrated System:**
- **37%** variance reduction (p<0.001)
- **18%** perturbation robustness improvement (p<0.001)  
- **23%** planning efficiency increase via Adapt-Plan
- **98%** traceability for audit compliance (TI=0.98)

---

## 🏗️ **System Architecture**

```
┌─────────────────────────────────────────────────────────────┐
│                    HB-Eval Framework                         │
│  Episode Expansion • Variance Analysis • Failure Clustering  │
└────────────────┬────────────────────────────────────────────┘
                 │ Detected Violations
                 ▼
┌─────────────────────────────────────────────────────────────┐
│                     Adapt-Plan                               │
│    PEI Monitoring • Real-time Correction • Efficiency        │
└────────────────┬────────────────────────────────────────────┘
                 │ Certified References
                 ▼
┌─────────────────────────────────────────────────────────────┐
│         EDM (Evaluation-Driven Memory)                       │
│   Episode Storage • FRR Tracking • Audit Trail (TI=0.98)    │
└────────────────┬────────────────────────────────────────────┘
                 │ Evidence Extraction
                 ▼
┌─────────────────────────────────────────────────────────────┐
│                    HCI-EDM                                   │
│  Performance-Grounded Explanations • Fairness Audit UI       │
└─────────────────────────────────────────────────────────────┘
```

**Data Flow:**  
Detection → Correction → Certification → Accountability

---

## 🚀 **Quick Start**

### **Installation**

```bash
git clone https://github.com/[anonymous-repo]/hb-eval-framework.git
cd hb-eval-framework
pip install -r requirements.txt
```

### **Basic Usage**

```python
from hb_eval import EpisodeLevelEvaluator
from adapt_plan import AdaptivePlanner
from edm import EpisodicMemory
from hci_edm import ExplanationGenerator

# Initialize integrated system
evaluator = EpisodeLevelEvaluator(K=5, perturbations=['paraphrase', 'context', 'format'])
planner = AdaptivePlanner(pei_threshold=0.5)
memory = EpisodicMemory()
explainer = ExplanationGenerator(memory)

# Evaluate agent with procedural fairness monitoring
reliability_profile = evaluator.evaluate(
    agent=your_agent,
    tasks=webarena_tasks,
    memory=memory,
    planner=planner
)

# Generate fairness audit report
fairness_report = explainer.generate_report(reliability_profile)
print(f"Variance: {reliability_profile.variance:.3f}")
print(f"Perturbation Robustness: {reliability_profile.robustness:.3f}")
print(f"Systematic Bias Detected: {reliability_profile.failure_clustering}")
```

### **Run Full Evaluation**

```bash
# WebArena evaluation (100 tasks, K=5 episodes each)
python scripts/evaluate_webarena.py --agent ReAct --K 5

# ALFWorld evaluation (50 tasks, K=5 episodes each)
python scripts/evaluate_alfworld.py --agent Reflexion --K 5

# End-to-end integrated system demo
python scripts/integrated_demo.py
```

---

## 📂 **Repository Structure**

```
hb-eval-framework/
├── hb_eval/                    # Core evaluation framework
│   ├── evaluator.py            # Episode-level evaluation
│   ├── perturbations.py        # Paraphrase/context/format variations
│   ├── metrics.py              # Variance, robustness, consistency
│   └── clustering.py           # Failure mode analysis
│
├── adapt_plan/                 # Real-time alignment correction
│   ├── planner.py              # Adaptive planning with PEI monitoring
│   ├── efficiency.py           # Planning Efficiency Index (PEI)
│   └── correction.py           # Replanning triggers
│
├── edm/                        # Certified episodic memory
│   ├── memory.py               # Episode storage with indexing
│   ├── certification.py        # FRR and TI computation
│   └── retrieval.py            # Similarity-based episode retrieval
│
├── hci_edm/                    # Human-interpretable explanations
│   ├── explanations.py         # Performance-grounded interpretation
│   ├── visualization.py        # Fairness audit dashboards
│   └── reporting.py            # Audit-ready reports
│
├── scripts/                    # Evaluation scripts
│   ├── evaluate_webarena.py
│   ├── evaluate_alfworld.py
│   └── integrated_demo.py
│
├── benchmarks/                 # Benchmark integration
│   ├── webarena_adapter.py
│   └── alfworld_adapter.py
│
├── examples/                   # Usage examples
│   ├── basic_evaluation.py
│   ├── fairness_audit.py
│   └── integrated_system.py
│
├── tests/                      # Unit and integration tests
├── docs/                       # Documentation
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📊 **Core Metrics**

### **HB-Eval Metrics**

| Metric | Formula | Fairness Dimension |
|--------|---------|-------------------|
| **Success Variance (σ²)** | `Var(𝟙_success)` | Procedural consistency |
| **Behavioral Consistency (BC)** | `1 - mean(EditDist)` | Decision stability |
| **Perturbation Robustness (PR)** | `1 - mean(ΔSR)` | Semantic fairness |
| **Failure Clustering (FC)** | Entropy of error distribution | Systematic bias detection |

### **Adapt-Plan Metrics**

| Metric | Formula | Purpose |
|--------|---------|---------|
| **Planning Efficiency Index (PEI)** | `GoalAchievement / ActionCost × (1 - Redundancy)` | Efficiency monitoring |

### **EDM Metrics**

| Metric | Formula | Purpose |
|--------|---------|---------|
| **Failure Resilience Rate (FRR)** | `#Recoveries / #Failures` | Learning from mistakes |
| **Traceability Index (TI)** | `LoggedActions / TotalActions` | Audit compliance |

---

## 🔬 **Reproducibility**

All results in the paper are fully reproducible:

```bash
# Reproduce Table 1 (Main results)
python scripts/reproduce_table1.py

# Reproduce Figure 1 (Reliability Gap)
python scripts/reproduce_figure1.py

# Reproduce Figure 2 (Workflow)
python scripts/reproduce_figure2.py

# Reproduce Figure 3 (Certified Reliability)
python scripts/reproduce_figure3.py

# Statistical significance tests
python scripts/run_statistical_tests.py
```

**Computational Requirements:**
- WebArena: ~42 GPU-hours for 100 tasks × 5 episodes
- ALFWorld: ~18 GPU-hours for 50 tasks × 5 episodes
- Total storage: ~10.4 GB for all traces

---

## 🎯 **Use Cases**

### **1. Pre-Deployment Fairness Assessment**
```python
# Assess procedural fairness before deployment
profile = evaluator.evaluate(candidate_agent, production_tasks)
if profile.variance > 0.12:
    print("⚠️ High variance detected - procedural unfairness risk")
if profile.failure_clustering['forms'] > 0.5:
    print("⚠️ Systematic bias: 50%+ failures on form tasks")
```

### **2. Real-Time Monitoring**
```python
# Monitor PEI during operation and trigger corrections
while agent.running:
    pei = planner.compute_pei(agent.current_trajectory)
    if pei < 0.5:
        corrected_plan = planner.replan(memory.retrieve_successful())
        agent.execute(corrected_plan)
```

### **3. Audit Trail Generation**
```python
# Generate compliance-ready audit reports
audit_report = explainer.generate_audit_report(
    time_range="2025-01-01 to 2025-01-31",
    agent_id="production-agent-v2.3"
)
# TI=0.98 ensures 98% of actions logged for regulatory review
```

### **4. Fairness-Aware Agent Selection**
```python
# Compare agents on fairness dimensions, not just accuracy
agents = [ReAct(), Reflexion(), TreeOfThought()]
profiles = [evaluator.evaluate(agent, tasks) for agent in agents]

# Rank by composite fairness score
fairness_ranking = sorted(profiles, 
    key=lambda p: (p.variance, -p.robustness, -p.consistency))
```

---

## 📈 **Benchmarks**

### **Supported Environments**

| Benchmark | Tasks | Modality | Difficulty |
|-----------|-------|----------|-----------|
| **WebArena** | 812 | Web navigation | High |
| **ALFWorld** | 134 | Embodied household | Medium |
| **SWE-bench** | 2,294 | Code generation | Very High |
| **Custom** | Any | Agent-defined | Variable |

### **Evaluated Architectures**

| Agent | Paradigm | Base Model |
|-------|----------|------------|
| **ReAct** | Single-pass reasoning | GPT-4-turbo |
| **Reflexion** | Iterative self-correction | GPT-4-turbo |
| **Tree-of-Thought** | Search-based planning | GPT-4-turbo |

---

## 🔄 **Extension Guide**

### **Adding New Agents**

```python
from hb_eval import AgentInterface

class MyCustomAgent(AgentInterface):
    def step(self, observation):
        # Your agent logic
        action = self.policy(observation)
        return action
    
    def reset(self):
        # Reset agent state
        pass

# Evaluate with HB-Eval
profile = evaluator.evaluate(MyCustomAgent(), tasks)
```

### **Adding New Perturbations**

```python
from hb_eval.perturbations import PerturbationBase

class MyPerturbation(PerturbationBase):
    def apply(self, task_description):
        # Transform task while preserving semantics
        return perturbed_description

evaluator.add_perturbation('my_perturbation', MyPerturbation())
```

### **Custom Fairness Metrics**

```python
from hb_eval.metrics import MetricBase

class DemographicParity(MetricBase):
    def compute(self, episodes, demographics):
        # Compute fairness metric
        return parity_score

evaluator.add_metric('demographic_parity', DemographicParity())
```

---

## 🧪 **Testing**

```bash
# Run all tests
pytest tests/

# Run specific test suites
pytest tests/test_hb_eval.py       # Core evaluation tests
pytest tests/test_adapt_plan.py    # Planning tests
pytest tests/test_edm.py           # Memory tests
pytest tests/test_hci_edm.py       # Explanation tests

# Run integration tests
pytest tests/integration/

# Generate coverage report
pytest --cov=hb_eval --cov-report=html
```

---

## 📖 **Documentation**

Detailed documentation is available in the `docs/` directory:

- **[Getting Started](docs/getting_started.md)** - Installation and basic usage
- **[API Reference](docs/api_reference.md)** - Complete API documentation
- **[Metrics Guide](docs/metrics.md)** - Detailed metric explanations
- **[Integration Guide](docs/integration.md)** - Integrating with existing systems
- **[Fairness Theory](docs/fairness_theory.md)** - Procedural fairness background
- **[Case Studies](docs/case_studies.md)** - Real-world applications

---

## 🤝 **Contributing**

Contributions are welcome after the review period. For now, please direct questions to the anonymous submission system.

---

## 📄 **Citation**

```bibtex
@inproceedings{anonymous2026hbeval,
  title={HB-Eval: Episode-Level Reliability Evaluation for Agentic AI Systems},
  author={Anonymous Authors},
  booktitle={ICLR 2026 Workshop on Algorithmic Fairness across Alignment procedures and Agentic systems},
  year={2026},
  note={Under review}
}
```

**Related Work:**
```bibtex
@inproceedings{anonymous2026adaptplan,
  title={Adapt-Plan: Efficiency-Aware Planning with Real-Time Alignment},
  author={Anonymous Authors},
  booktitle={ICLR 2026 Workshop on AFAA},
  year={2026},
  note={Under review}
}

@inproceedings{anonymous2026edm,
  title={EDM: Certified Episodic Memory for Accountable Agentic Systems},
  author={Anonymous Authors},
  booktitle={ICLR 2026 Workshop on AFAA},
  year={2026},
  note={Under review}
}

@inproceedings{anonymous2026hciedm,
  title={HCI-EDM: Performance-Grounded Interpretability for Fair Agents},
  author={Anonymous Authors},
  booktitle={ICLR 2026 Workshop on AFAA},
  year={2026},
  note={Under review}
}
```

---

## 🛡️ **License**

This project is licensed under the **Apache License 2.0**.

---

## 💬 **FAQ**

**Q: Why focus on procedural fairness instead of demographic fairness?**  
A: Procedural fairness (consistent treatment of equivalent scenarios) is a prerequisite for responsible deployment. We focus on behavioral consistency as a measurable dimension of fairness. Demographic fairness integration is planned for future work.

**Q: How does HB-Eval differ from robustness testing?**  
A: Robustness testing typically measures worst-case adversarial degradation. HB-Eval measures typical-case variation under realistic, benign perturbations (how users naturally phrase tasks) to assess procedural consistency.

**Q: Can HB-Eval guarantee formal fairness?**  
A: No. HB-Eval provides empirical characterization of procedural fairness through behavioral measurement. It complements but does not replace formal verification methods.

**Q: What is the computational overhead?**  
A: K=5 episodes increases evaluation cost 3-5× compared to single-episode benchmarks. This is acceptable for pre-deployment assessment and periodic auditing but may be prohibitive for rapid iteration.

**Q: Does this work with LLM-based agents only?**  
A: No. HB-Eval is model-agnostic and evaluates system-level behavior regardless of the underlying architecture (rule-based, classical ML, or LLMs).

**Q: When will the code be fully released?**  
A: Full release with complete documentation, tutorials, and pre-trained models will follow upon paper acceptance.

---

## 📧 **Contact**

For questions about this anonymous submission, please use the conference submission system.

**After acceptance, contact information will be provided.**

---

<p align="center">
  <b>Anonymous Submission for ICLR 2026 AFAA Workshop</b><br>
  <i>"Reliability is not orthogonal to fairness—it is constitutive of it."</i>
</p>

---

## 🔗 **Related Resources**

- **ICLR 2026 AFAA Workshop**: [Link will be added]
- **Supplementary Materials**: Available in submission system
- **Interactive Demo**: [Link will be added upon acceptance]

---

## 🌟 **Acknowledgments**

We thank the anonymous reviewers for their valuable feedback and the organizers of the ICLR 2026 AFAA Workshop for creating this important venue for fairness research.

---

**Last Updated:** January 2026  
**Status:** Under Anonymous Review for ICLR 2026 AFAA Workshop
