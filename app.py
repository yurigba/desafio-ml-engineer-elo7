from fastapi import FastAPI
import pickle

from model_inference.nodes import (
    format_input_fastapi,
    apply_vectorizer,
    apply_svm
)

from model_inference.types import (
    Categories,
    Products
)

app = FastAPI()

with open("/home/elo7/assets/vectorizer.pickle", "rb") as v:
    vectorizer = pickle.load(v)
    
with open("/home/elo7/assets/model.pickle", "rb") as m:
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