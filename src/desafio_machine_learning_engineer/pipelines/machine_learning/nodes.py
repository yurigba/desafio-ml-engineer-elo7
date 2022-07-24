"""
Nós utilizados para o treino e teste de modelo
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

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
