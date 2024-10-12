from unittest.mock import patch

from app.repository.product_repo import ProductRepo
from app.schemas.product_schema import ProductBase


@patch("sqlalchemy.orm.session.Session")
def test_add_products(db):
    # Init repository with a mock
    repo = ProductRepo(db)
    biscuit = {
        "name": "Farmlite Oats & Chocolate",
        "description": "With goodness of oats and delicious chocolates, enjoy this delectable cookie",
        "price": 50.0,
        "qty": 1,
    }
    new_product = ProductBase(**biscuit)
    repo.add_product(new_product)
    # object has been called exactly 1 time.
    db.add.assert_called_once()


@patch("sqlalchemy.orm.session.Session")
def test_get_products(db):
    # Init repository with a mock
    repo = ProductRepo(db)
    repo.get_all_products()
    db.query.assert_called_once()
