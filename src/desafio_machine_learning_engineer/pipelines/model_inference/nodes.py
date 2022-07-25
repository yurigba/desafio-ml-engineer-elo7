import re

def format_input(input):
    
    """
    FORMAT INPUT - checa o input e formata para ser aplicado no vectorizer
    """
    
    titles = []
    
    # Tratamento de excecoes
    # 1. checa se a chave products esta presente
    if "products" in input:
        for product in input["products"]:
            
            # 2. checa se a chave title esta presente e se o que tem dentro e string
            if "title" in product and isinstance(product["title"], str):
                
                # 3. troca os numeros pelo token NUM
                titles.append(re.sub(r"\d+", "NUM", product["title"]))
                
            else:
                return {
                    "products": [],
                    "status": 400
                }
            
        return {
            "products": titles,
            "status": 200
            }
    
    else:
        return {
            "products": [],
            "status": 400
            }

def apply_vectorizer(vectorizer, input):
    
    if input["status"] == 200:
    
        return {
            "vectorized_products": vectorizer.transform(input["products"]),
            "status": 200
            }
        
    else:
        
        return {
            "vectorized_products": [],
            "status": 400
        }
        

def apply_svm(model, input):
    
    if input["status"] == 200:
    
        return {
            "categories": list(model.predict(input["vectorized_products"]))
        }
        
    else:
        
        return {
            "categories": [],
            "status": 400
        }