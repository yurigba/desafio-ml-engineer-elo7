"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from desafio_machine_learning_engineer.pipelines.machine_learning.pipeline import create_pipeline as ml_pipeline
from desafio_machine_learning_engineer.pipelines.model_inference.pipeline import create_pipeline as inference_pipeline

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {
        "__default__": pipeline([ml_pipeline()]),
        "inference": inference_pipeline()
        }
