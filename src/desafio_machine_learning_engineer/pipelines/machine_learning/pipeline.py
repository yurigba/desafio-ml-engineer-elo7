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
    apply_vectorizer,
    data_loader
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node( # Filtra as colunas necessarias
            name="carregamento_de_dados",
            func= data_loader,
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
            name="transformacao_de_dados_de_treino",
            func=fit_vectorizer,
            inputs="train_dataset",
            outputs=["vectorizer", "train_x_input"]
        ),
        node(
            name="modelagem_treino",
            func=fit_svm,
            inputs=["train_x_input", "train_dataset"],
            outputs="model"
        ),
        node(
            name="transformacao_de_dados_de_teste",
            func=apply_vectorizer,
            inputs=["vectorizer","test_dataset"],
            outputs="test_x_input"
        ),
        node(
            name="modelagem_teste",
            func=apply_model,
            inputs=["model", "test_x_input"],
            outputs="y_pred"
        ),
        node(
            name="validacao_de_modelo",
            func=lambda df, y_pred: classification_report(df["category"], y_pred),
            inputs=["test_dataset", "y_pred"],
            outputs="classification_report"
        )
    ])
