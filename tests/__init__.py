"""
HB-Eval Test Suite
------------------
This package contains the validation scripts for the HB-Eval framework.
It ensures numerical consistency between the Core Framework and Mobile Demos.
"""

__version__ = "1.0.0"
__test_status__ = "Verified: Perfect Match"

# Optional: Configuration for all tests
import random

# Global seed for all tests to ensure scientific reproducibility
TEST_SEED = 42

def setup_test_env():
    """Initializes the environment for consistent testing."""
    random.seed(TEST_SEED)
    # print(f"[HB-Eval Tests] Environment initialized with seed: {TEST_SEED}")