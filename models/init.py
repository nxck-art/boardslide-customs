from flask_sqlalchemy import SQLAlchemy
from models import db
import models

# import models for SQLAlchemy
from .product import Product
from .customer import Customer
from .order import Order
from .order_item import OrderItem
from .skateboard import Skateboard