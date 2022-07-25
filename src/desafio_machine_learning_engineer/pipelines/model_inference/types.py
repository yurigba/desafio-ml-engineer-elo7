from pydantic import BaseModel
from typing import List

class Title(BaseModel):
    title: str
    
    class Config:
        schema_extra = {
            "examples": ["Lembrancinha"]
        }
    
class Products(BaseModel):
    
    products: List[Title]
    
    class Config:
        schema_extra = {
            "example": {
                "products": [
                    {
                        "title": "Lembrancinha"
                        },
                    {
                        "title": "Carrinho de Bebê"
                        }
                ]
            },
            "examples": {
                "working":{
                    "products": [
                        {
                            "title": "Lembrancinha"
                            }
                    ]
                },
                "work2":{
                    "products": [
                        {
                            "title": "Lembrancinha"
                            },
                        {
                            "title": "abc"
                            }
                    ]
                }
            }
        }

class Categories(BaseModel):
    categories: List[str]
    
    class Config:
        schema_extra = {
            "example": {
                "categories": [
                    "<category1>", "<category2>"
                    ]
                }
            }
