from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer

from app.cfg.database import Base



# 2. Definición de la Entidad (Tabla 'products')
class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    numeros: Mapped[int] = mapped_column(Integer, default=20)

    def __repr__(self):
        return f"<Product(id={self.id}, nombre='{self.nombre}')>"