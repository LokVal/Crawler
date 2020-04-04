from dataclasses import dataclass
from datetime import datetime


@dataclass
class Manufacturer:
    id: str
    name: str
    create_date: datetime
    mod_date: datetime


@dataclass
class ProductBrand:
    id: str
    name: str
    manufacturer_id: str
    create_date: datetime
    mod_date: datetime


@dataclass
class Product:
    id: str
    asin: str
    model_number: str
    url: str
    product_title: str
    price: float
    bsr: float
    customer_rating: int
    rating_amount: int
    product_brand_id: str
    published: datetime
    dim_x: float
    dim_y: float
    dim_z: float
    weight: float
    shipping_weight: float
    create_date: datetime
    mod_date: datetime


@dataclass
class ProductAudit:
    id: str
    property_name: str
    type: str
    old_value: str
    new_value: str
    create_date: datetime
    mod_date: datetime
