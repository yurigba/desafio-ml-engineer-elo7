"""
Pipeline básica de treino de modelo usando Kedro
"""

from kedro.pipeline import Pipeline, node, pipeline
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from .nodes import (
    fit_svm,
    fit_vectorizer,
    apply_model,
    apply_vectorizer
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node( # Filtra as colunas necessarias
            name="filter_columns",
            func= lambda df: df[["title", "category"]],
            inputs= "elo7_recruitment_dataset",
            outputs= "input_dataset"
        ),
        node(
            name="split_dataset",
            func= (
                lambda df, params: 
                    train_test_split(
                        df,
                        random_state=params["random_state"],
                        test_size=params["test_size"]
                        )
                ),
            inputs= ["input_dataset", "params:split_params"],
            outputs= ["train_dataset", "test_dataset"]
        ),
        node(
            name="fit_vectorizer",
            func=fit_vectorizer,
            inputs="train_dataset",
            outputs=["vectorizer", "train_x_input"]
        ),
        node(
            name="fit_svm",
            func=fit_svm,
            inputs=["train_x_input", "train_dataset"],
            outputs="model"
        ),
        node(
            name="apply_vectorizer",
            func=apply_vectorizer,
            inputs=["vectorizer","test_dataset"],
            outputs="test_x_input"
        ),
        node(
            name="apply_svm",
            func=apply_model,
            inputs=["model", "test_x_input"],
            outputs="y_pred"
        ),
        node(
            name="classification_report",
            func=lambda df, y_pred: classification_report(df["category"], y_pred),
            inputs=["test_dataset", "y_pred"],
            outputs="classification_report"
        )
    ])
