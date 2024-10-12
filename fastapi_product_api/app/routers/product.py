import logging

from ..database import db
from fastapi import APIRouter

from ..repository.product_repo import ProductRepo
from ..schemas.product_schema import ProductBase, Status

router = APIRouter()

logger = logging.getLogger(__name__)

# Init repository
repo = ProductRepo(db)


# Add new Product
@router.post("/product/")
async def add_product(prod: ProductBase):
    logger.info("Got request for adding new product")
    repo.add_product(prod)
    return '{"result": "Success"}'


# Get specifc Product
@router.get("/product/{product_id}", response_model=ProductBase)
async def get_product(product_id: int):
    logger.info("Got request for fetching a single product")
    product = repo.get_product(product_id)
    return product


# Get All Products
@router.get("/product/all")
async def get_products():
    logger.info("Got request for fetching all products")
    all_products = repo.get_all_products()
    return all_products


# Update an existing Product
@router.put("/product/{product_id}", response_model=ProductBase)
async def update_product(product_id: int, prod: ProductBase):
    logger.info("Got request for updating  product")
    updated = repo.update_product(product_id, prod)
    return updated


# Remove an existing Product
@router.delete("/product/{product_id}", response_model=Status)
async def delete_product(product_id: int):
    logger.info("Got request for deleting product")
    repo.delete_product(product_id)
    return Status(message=f"Deleted product {product_id}")
