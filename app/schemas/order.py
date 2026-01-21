from pydantic import BaseModel

class OrderCreate(BaseModel):
    product_id: int
    quantity: int

class OrderOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price: float

    class Config:
        from_attributes = True
