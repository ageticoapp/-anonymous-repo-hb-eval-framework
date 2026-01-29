"""
HB-Eval: Behavioral Certification for Agentic AI

A framework for evaluating AI agent reliability through systematic stress testing
and multi-dimensional metrics that distinguish capability from reliability.

Key Components:
    - Metrics: FRR, PEI, IRS, ARR, TI
    - Stress Testing: Fault injection, adversarial attacks
    - Certification: Three-tier deployment framework
    - RL Analysis: Withdrawal pathology detection

Example:
    >>> from hb_eval import StressTester, MetricsCalculator
    >>> tester = StressTester(domains=['healthcare'])
    >>> results = tester.evaluate(agent, episodes=100)
    >>> metrics = MetricsCalculator.compute_all(results)
    >>> print(f"FRR: {metrics['FRR']:.2f}%")

Citation:
    Anonymous et al. (2026). HB-Eval: Toward Verifiable Behavioral 
    Certification for Agentic AI. VerifAI Workshop @ ICLR 2026.

License:
    Apache 2.0
"""

__version__ = "0.1.0"
__author__ = "Anonymous Authors"
__license__ = "Apache 2.0"

# Core imports (to be implemented post-acceptance)
try:
    from .metrics import (
        MetricsCalculator,
        FailureResilienceRate,
        PlanningEfficiencyIndex,
        IntentionalRecoveryScore,
        AdversarialResilienceRate,
        TraceabilityIndex
    )
    
    from .stress_testing import (
        StressTester,
        FaultInjector,
        AdversarialAttacker
    )
    
    from .environments import (
        Environment,
        HealthcareEnvironment,
        LogisticsEnvironment,
        CodingEnvironment
    )
    
    from .certification import (
        CertificationFramework,
        Tier1Operational,
        Tier2Supervised,
        Tier3SafetyCritical
    )
    
except ImportError:
    # During development/submission phase
    pass

__all__ = [
    # Version info
    '__version__',
    '__author__',
    '__license__',
    
    # Core classes (available post-full implementation)
    'MetricsCalculator',
    'StressTester',
    'Environment',
    'CertificationFramework',
]


def get_version():
    """Return current version."""
    return __version__


def citation():
    """Return citation information."""
    return """
@inproceedings{anonymous2026hbeval,
  title={HB-Eval: Toward Verifiable Behavioral Certification for Agentic AI},
  author={Anonymous Authors},
  booktitle={VerifAI Workshop @ ICLR 2026},
  year={2026},
  url={https://anonymous.4open.science/r/hb-eval-XXXX}
}
"""


# Package metadata
PACKAGE_INFO = {
    'name': 'hb-eval',
    'version': __version__,
    'description': 'Behavioral Certification Framework for Agentic AI',
    'author': __author__,
    'license': __license__,
    'url': 'https://anonymous.4open.science/r/hb-eval-XXXX',
    'keywords': [
        'ai-safety',
        'agent-evaluation', 
        'behavioral-certification',
        'reinforcement-learning',
        'verification'
    ],
    'python_requires': '>=3.8',
}
