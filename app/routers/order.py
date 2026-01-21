from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine
from app.models.order import Order
from app.models.product import Product
from app.dependencies import get_db, get_current_user, get_current_admin
from app.schemas.order import OrderCreate, OrderOut

Order.metadata.create_all(bind=engine)

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderOut)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == order.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    total_price = product.price * order.quantity

    new_order = Order(
        user_id=user.id,
        product_id=product.id,
        quantity=order.quantity,
        total_price=total_price
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@router.get("/", response_model=list[OrderOut])
def list_orders(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    if user.is_admin:
        return db.query(Order).all()

    return db.query(Order).filter(Order.user_id == user.id).all()
