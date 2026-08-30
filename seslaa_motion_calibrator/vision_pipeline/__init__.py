"""Monocular detection, tracking, motion, and risk assessment pipeline."""

from .config import PipelineConfig

__all__ = ["PipelineConfig", "MonocularVisionPipeline"]


def __getattr__(name):
	if name == "MonocularVisionPipeline":
		from .pipeline import MonocularVisionPipeline
		return MonocularVisionPipeline
	raise AttributeError(name)