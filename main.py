from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)


# uvicorn main:app --reload

# Rest APIs
# Get -> leitura/pegar
# Post -> enviar/criar
# Put/Patch -> editar
# Delete -> deletar