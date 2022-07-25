"""
Nós utilizados para o treino e teste de modelo
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

def data_loader(df):
    
    out_df = pd.DataFrame(
        { # Trocamos os numeros pela expressao NUM usando regex
            "title": df["title"].replace(r"\d+", 'NUM', regex=True),
            "category": df["category"]
            }
        )
    
    return out_df

def fit_vectorizer(train_input):
    
    cv = CountVectorizer()
    X_input_transformed = cv.fit_transform(train_input["title"])
    
    return cv, X_input_transformed

def fit_svm(transformed_input, train_input):
    
    svm = SVC()
    svm.fit(transformed_input, train_input["category"])
    
    return svm

def apply_vectorizer(vectorizer, test_input):
    
    return vectorizer.transform(test_input["title"])

def apply_model(model, vectorized_input):
    
    return model.predict(vectorized_input)
