from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, product, order
from app.models.user import User
from app.models.product import Product
from app.models.order import Order

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Coffee Order API")

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(order.router)
