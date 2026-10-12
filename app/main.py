from cfg.database import engine
from app.models.products import Base
from fastapi import FastAPI
# 1. Crear la instancia de FastAPI (¡Esto es lo que faltaba!)
app = FastAPI()

# Esto lee todos los modelos que heredan de Base y crea las tablas si no existen
Base.metadata.create_all(bind=engine)