# Pipeline machine_learning

Pipeline básica para treinamento de um modelo de machine learning
para determinar a categoria de um título de produto

## Visão Geral

Essa pipeline basicamente pega o dataset público elo7, formata para ter apenas as colunas
de interesse, troca os números pelo token "NUM" e aplica um CountVectorizer simples,
para então treinar um modelo SVM.

## Inputs da Pipeline

- Dataset público Elo7

## Outputs da Pipeline

- Vectorizer localizado em data/06_models/vectorizer.pickle
- Modelo localizado em data/06_models/model.pickle
- Métricas de modelo localizadas em data/08_reporting/classification_report.txt
