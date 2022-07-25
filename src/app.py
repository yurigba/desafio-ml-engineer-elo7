from fastapi import FastAPI
import pickle

from desafio_machine_learning_engineer.pipelines.model_inference.nodes import (
    format_input_fastapi,
    apply_vectorizer,
    apply_svm
)

from desafio_machine_learning_engineer.pipelines.model_inference.types import (
    Categories,
    Products
)

app = FastAPI()

with open("../data/06_models/vectorizer.pickle", "rb") as v:
    vectorizer = pickle.load(v)
    
with open("../data/06_models/model.pickle", "rb") as m:
    model = pickle.load(m)

@app.post("/inference", response_model=Categories)
async def make_inference(
    input: Products
    ) -> Categories:
    
    formatted_input = format_input_fastapi(input)
    vectorized_input = apply_vectorizer(vectorizer, formatted_input)
    model_output = apply_svm(model, vectorized_input)
    
    return {
        "categories": model_output["categories"]
        }