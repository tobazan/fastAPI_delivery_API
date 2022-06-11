from fastapi import FastAPI
import uvicorn

from routes.users_routes import users_router
from routes.products_routes import products_router
from routes.pay_methods_routes import pay_methods_router
from routes.carts_routes import carts_router

from models.users_models import *
from models.products_models import *
from models.pay_methods_models import *
from models.carts_models import *

app = FastAPI()

app.include_router(users_router)
app.include_router(products_router)
app.include_router(pay_methods_router)
app.include_router(carts_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=8080, reload=True)