# FastAPI routers
from fastapi import APIRouter
from ..models.schemas import Product
from typing import List

router = APIRouter(prefix="/products", tags=["products"])

products: List[Product] = []

@router.post("", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product

@router.get("", response_model=List[Product])
def list_products():
    return products
