"""
This is a boilerplate pipeline 'model_inference'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import apply_vectorizer, apply_svm

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            name="inference_vectorizer",
            func=apply_vectorizer,
            inputs=["vectorizer", "inference_test"],
            outputs="vectorized_inference_test"
        ),
        node(
            name="inference_model",
            func=apply_svm,
            inputs=["model", "vectorized_inference_test"],
            outputs="inference_model_output"
        )
    ])
