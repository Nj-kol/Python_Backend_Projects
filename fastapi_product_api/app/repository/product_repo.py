from ..models.product_models import Product
from ..schemas.product_schema import ProductBase
from sqlalchemy.orm.session import Session


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d


class ProductRepo:

    # parameterized constructor
    def __init__(self, db: Session):
        self.db = db

    def add_product(self, product: ProductBase):
        new_product = Product(product.name, product.description, product.price, product.qty)
        self.db.add(new_product)
        self.db.commit()

    def get_product(self, id: int):
        product = self.db.query(Product).get(id)
        # product = Product.query.get(id)
        pyd_model = ProductBase(**row2dict(product))
        return pyd_model

    def get_all_products(self):
        all_products = self.db.query(Product).all()
        return all_products

    def update_product(self, id, updated_product: ProductBase):
        product = self.db.query(Product).get(id)
        product.name = updated_product.name
        product.description = updated_product.description
        product.price = updated_product.price
        product.qty = updated_product.qty
        self.db.commit()
        pyd_model = ProductBase(**row2dict(product))
        return pyd_model

    def delete_product(self, id):
        product = self.db.query(Product).get(id)
        self.db.delete(product)
        self.db.commit()
