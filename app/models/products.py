from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, Integer

# 1. Clase Base para que SQLAlchemy reconozca los modelos
class Base(DeclarativeBase):
    pass

# 2. Definición de la Entidad (Tabla 'products')
class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, default=0)

    def __repr__(self):
        return f"<Product(id={self.id}, nombre='{self.nombre}')>"