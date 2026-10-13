from fastapi import APIRouter, Depends

from app.models.products import ProductModel
from app.cfg.database import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.schemas import ProductSchema

router = APIRouter(
    prefix="/products",
    tags=["products"],
    
)

@router.post("/")
def create_product(product: ProductSchema, db: Session = Depends(get_db)):
    nuevo_producto = ProductModel(nombre=product.nombre, precio=product.precio, stock=product.stock)
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

