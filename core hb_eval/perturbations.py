"""
Semantic-Preserving Perturbations

Applies benign variations to task specifications while maintaining
semantic equivalence, testing procedural fairness under realistic
deployment conditions.
"""

from abc import ABC, abstractmethod
from typing import Dict, List
import re


class PerturbationBase(ABC):
    """Base class for semantic-preserving perturbations."""
    
    @abstractmethod
    def apply(self, text: str) -> str:
        """Apply perturbation to text."""
        pass


class ParaphrasePerturbation(PerturbationBase):
    """
    Linguistic paraphrasing while preserving semantics.
    
    Tests robustness to natural language variation:
    how users might phrase the same request differently.
    """
    
    def __init__(self):
        # Simple rule-based paraphrasing
        # In production, use LLM (GPT-4) with prompt:
        # "Rewrite the following preserving exact meaning and requirements"
        self.synonyms = {
            'find': 'locate',
            'get': 'retrieve',
            'show': 'display',
            'click': 'select',
            'navigate': 'go',
            'search': 'look for'
        }
    
    def apply(self, text: str) -> str:
        """Apply synonym substitution."""
        result = text
        for original, synonym in self.synonyms.items():
            # Case-insensitive replacement
            pattern = re.compile(r'\b' + original + r'\b', re.IGNORECASE)
            result = pattern.sub(synonym, result)
        return result


class ContextPerturbation(PerturbationBase):
    """
    Add or remove non-essential contextual information.
    
    Tests robustness to information density changes:
    some users provide minimal instructions, others verbose context.
    """
    
    def __init__(self, mode: str = 'add'):
        """
        Args:
            mode: 'add' to prepend context, 'remove' to strip context
        """
        self.mode = mode
        self.context_templates = [
            "Please help me with the following task: ",
            "I need assistance with: ",
            "Could you please: ",
            "Task to complete: "
        ]
    
    def apply(self, text: str) -> str:
        """Add or remove context."""
        if self.mode == 'add':
            # Prepend contextual preamble
            import random
            preamble = random.choice(self.context_templates)
            return preamble + text
        else:
            # Remove common preambles
            for template in self.context_templates:
                if text.startswith(template):
                    return text[len(template):]
            return text


class FormatPerturbation(PerturbationBase):
    """
    Alter presentation format while preserving content.
    
    Tests robustness to syntactic structure:
    numbered lists vs paragraphs vs bullet points.
    """
    
    def __init__(self):
        self.format_types = ['numbered', 'bullets', 'paragraph']
    
    def apply(self, text: str) -> str:
        """Convert between formatting styles."""
        # Detect current format
        if self._is_numbered(text):
            return self._to_bullets(text)
        elif self._is_bullets(text):
            return self._to_paragraph(text)
        else:
            return self._to_numbered(text)
    
    def _is_numbered(self, text: str) -> bool:
        """Check if text uses numbered list."""
        return bool(re.search(r'^\d+\.', text, re.MULTILINE))
    
    def _is_bullets(self, text: str) -> bool:
        """Check if text uses bullet points."""
        return bool(re.search(r'^[•\-\*]', text, re.MULTILINE))
    
    def _to_bullets(self, text: str) -> str:
        """Convert numbered list to bullets."""
        return re.sub(r'^\d+\.\s*', '• ', text, flags=re.MULTILINE)
    
    def _to_numbered(self, text: str) -> str:
        """Convert to numbered list."""
        lines = text.split('\n')
        numbered = []
        count = 1
        for line in lines:
            if line.strip():
                # Remove existing bullets
                cleaned = re.sub(r'^[•\-\*]\s*', '', line)
                numbered.append(f"{count}. {cleaned}")
                count += 1
            else:
                numbered.append(line)
        return '\n'.join(numbered)
    
    def _to_paragraph(self, text: str) -> str:
        """Convert list to paragraph."""
        # Remove numbering and bullets
        cleaned = re.sub(r'^(\d+\.|[•\-\*])\s*', '', text, flags=re.MULTILINE)
        # Join lines
        lines = [line.strip() for line in cleaned.split('\n') if line.strip()]
        return ' '.join(lines)


class PerturbationPipeline:
    """
    Apply multiple perturbations in sequence.
    
    Useful for stress-testing under combined variations.
    """
    
    def __init__(self, perturbations: List[PerturbationBase]):
        self.perturbations = perturbations
    
    def apply(self, text: str) -> str:
        """Apply all perturbations sequentially."""
        result = text
        for pert in self.perturbations:
            result = pert.apply(result)
        return result


# Utility functions for validation
def semantic_similarity(text1: str, text2: str) -> float:
    """
    Estimate semantic similarity between original and perturbed text.
    
    In production, use sentence embeddings (SBERT) for validation.
    This is a placeholder using word overlap.
    """
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    
    intersection = words1 & words2
    union = words1 | words2
    
    return len(intersection) / len(union) if union else 0.0


def validate_perturbation(
    original: str,
    perturbed: str,
    min_similarity: float = 0.7
) -> bool:
    """
    Validate that perturbation preserves semantics.
    
    Returns True if semantic similarity exceeds threshold.
    """
    similarity = semantic_similarity(original, perturbed)
    return similarity >= min_similarity