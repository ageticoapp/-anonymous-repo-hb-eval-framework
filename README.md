# 📦 HB-Eval Anonymous Submission Package

**Paper Title:** HB-Eval: Toward Verifiable Behavioral Certification for Agentic AI  
**Venue:** VerifAI Workshop @ ICLR 2026  
**Submission Date:** February 5, 2026

---

## 📂 Package Contents

```
hb-eval-submission/
├── README.md                       # This file
├── LICENSE                        # Apache 2.0 license
├── CITATION.cff                   # Citation metadata
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git exclusions
│
├── demos/
│   ├── withdrawal_demo.py         # Theorem C.1 demonstration
│   └── multiagent_demo.py         # Theorem C.3 demonstration
│
├── hb_eval/
│   └── __init__.py                # Package initialization
│
└── docs/
    └── QUICKSTART.md              # Quick start guide
```

---

## 🚀 Quick Verification

### **Test the demos** (2 minutes total)

```bash
# Navigate to submission directory
cd hb-eval-submission

# Install dependencies
pip install numpy scipy pandas

# Run withdrawal demo
python demos/withdrawal_demo.py

# Run multi-agent demo
python demos/multiagent_demo.py
```

**Expected outputs:**
- Withdrawal demo: `Final caution: 0.000`
- Multi-agent demo: `Final cautions: [0.000, 0.000, 0.000]`

---

## 📋 Submission Components

### **1. Main Paper**
- **File**: `HB_Eval_ICLR2026.pdf` (to be uploaded separately)
- **Length**: 8 pages + 35 pages appendices
- **Format**: ICLR 2026 LaTeX template

### **2. Supplementary Code** (this package)
- **Demos**: Executable Python scripts
- **Documentation**: Comprehensive guides
- **License**: Apache 2.0 (open source)

### **3. Cover Letter**
- **File**: `COVER_LETTER.txt`
- **Content**: Novelty, limitations, transparency commitment

---

## 🔗 Repository Access

**Anonymous Repository:**  
https://anonymous.4open.science/r/hb-eval-XXXX

*(Link to be included in paper footnote and OpenReview submission)*

---

## ✅ Reproducibility

All results in the paper are **fully reproducible**:

- **Random seeds**: Fixed (seed=42)
- **Platform**: Ubuntu 24.04, Python 3.8+
- **Runtime**: 
  - Demos: <5 minutes (CPU)
  - Full experiments: ~5 hours (A100 GPU)
- **Cost**: ~$200 on cloud compute

---

## 📧 Contact

**During Review:** All communication via OpenReview  
**Post-Acceptance:** Author info will be de-anonymized

---

## 🎯 Key Claims to Verify

1. **Withdrawal Pathology**: `demos/withdrawal_demo.py`
   - Claim: Unconstrained RL → caution collapses to 0
   - Verification: Run script, observe final caution ≈ 0.0

2. **Nash Equilibrium**: `demos/multiagent_demo.py`
   - Claim: Multi-agent amplifies withdrawal
   - Verification: Run script, observe all agents → 0.0

3. **Reproducibility**: Both demos
   - Claim: Deterministic with seed=42
   - Verification: Run multiple times, identical results

---

## ⚖️ Ethical Statement

- No human subjects research
- No sensitive data
- Simulated environments only
- Open source commitment
- Transparent about limitations

---

## 🙏 Acknowledgments

We thank:
- VerifAI workshop organizers
- Anonymous reviewers (in advance)
- AI safety research community

---

**Prepared with care for the research community** ❤️

*Last updated: January 28, 2026*
