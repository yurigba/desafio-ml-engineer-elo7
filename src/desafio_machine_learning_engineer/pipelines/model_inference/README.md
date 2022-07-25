# Pipeline model_inference

Pipeline a ser utilizada na API que servirá o modelo

## Visão Geral

A pipeline espera um JSON com a chave "products", com uma lista de dicts
com a chave "title", cada um com uma string. Ele verifica se está nesse formato.

Caso esteja no formato esperado, retorna um outro dict com a chave "categories"
que deve ser uma lista com strings.

## Pipeline inputs

- Dict de input localizado em data/01_raw/test_inference.json
- Vectorizer localizado em data/06_models/vectorizer.pickle
- Modelo localizado em data/06_models/model.pickle

## Pipeline outputs

Dict formatado com categorias em data/07_model_output/inference_model_output.json