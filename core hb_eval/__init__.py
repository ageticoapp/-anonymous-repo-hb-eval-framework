"""
HB-Eval: Episode-Level Reliability Evaluation Framework

This module provides the core evaluation infrastructure for assessing
procedural fairness in agentic AI systems through repeated episode-level
behavioral analysis under controlled perturbations.

Key Components:
- EpisodeLevelEvaluator: Main orchestrator for K-episode evaluation
- Metrics: Variance, consistency, robustness, clustering
- Perturbations: Semantic-preserving task variations
- ReliabilityProfile: Aggregated fairness assessment

Anonymous submission for ICLR 2026 AFAA Workshop.
"""

__version__ = "1.0.0"
__status__ = "Anonymous Review"

from .evaluator import EpisodeLevelEvaluator
from .metrics import (
    compute_variance,
    compute_behavioral_consistency,
    compute_perturbation_robustness,
    compute_failure_clustering
)
from .perturbations import (
    ParaphrasePerturbation,
    ContextPerturbation,
    FormatPerturbation
)
from .reliability_profile import ReliabilityProfile

__all__ = [
    "EpisodeLevelEvaluator",
    "compute_variance",
    "compute_behavioral_consistency",
    "compute_perturbation_robustness",
    "compute_failure_clustering",
    "ParaphrasePerturbation",
    "ContextPerturbation",
    "FormatPerturbation",
    "ReliabilityProfile"
]

# Compatibility note for mobile demos:
# The mobile_demos/ directory contains simplified, zero-dependency 
# implementations that validate core algorithmic logic using only
# Python's standard library. Those demos are functionally equivalent
# to this production framework but designed for:
# - Educational purposes (teaching core concepts)
# - Rapid prototyping (testing without infrastructure)
# - Accessibility (running on mobile/embedded devices)
#
# This framework (hb_eval/) is the production-grade implementation
# designed for:
# - Real agent evaluation (ReAct, Reflexion, ToT, etc.)
# - Full benchmark integration (WebArena, ALFWorld, etc.)
# - Comprehensive metrics (variance, consistency, robustness, clustering)
# - Statistical rigor (significance tests, confidence intervals)"""
HB-Eval: Episode-Level Reliability Evaluation Framework

This module provides the core evaluation infrastructure for assessing
procedural fairness in agentic AI systems through repeated episode-level
behavioral analysis under controlled perturbations.

Anonymous submission for ICLR 2026 AFAA Workshop.
"""

__version__ = "1.0.0"
__status__ = "Anonymous Review"

from .evaluator import EpisodeLevelEvaluator
from .metrics import (
    compute_variance,
    compute_behavioral_consistency,
    compute_perturbation_robustness,
    compute_failure_clustering
)
from .perturbations import (
    ParaphrasePerturbation,
    ContextPerturbation,
    FormatPerturbation
)
from .clustering import FailureClusterAnalyzer
from .reliability_profile import ReliabilityProfile

__all__ = [
    "EpisodeLevelEvaluator",
    "compute_variance",
    "compute_behavioral_consistency",
    "compute_perturbation_robustness",
    "compute_failure_clustering",
    "ParaphrasePerturbation",
    "ContextPerturbation",
    "FormatPerturbation",
    "FailureClusterAnalyzer",
    "ReliabilityProfile"
]