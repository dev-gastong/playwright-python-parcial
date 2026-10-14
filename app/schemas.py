# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field

class ProductSchema(BaseModel):

    nombre: str = Field(min_length=3, max_length=50)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)
    
    




