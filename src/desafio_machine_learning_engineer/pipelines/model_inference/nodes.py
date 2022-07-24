"""
This is a boilerplate pipeline 'model_inference'
generated using Kedro 0.18.2
"""

def apply_vectorizer(vectorizer, input):
    
    titles = []
    
    for product in input["products"]:
        titles.append(product["title"])
        
    return vectorizer.transform(titles)

def apply_svm(model, input):
    
    return {
        "categories": list(model.predict(input))
    }