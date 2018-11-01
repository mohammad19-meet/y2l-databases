from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name,price,quantity,description):
  product_object = Product(
      name = name,
      price=price,
      quantity=quantity,
      description=description)
  session.add(product_object)
  session.commit()


def update_product(name, price):
  product_object = session.query(
      Product).filter_by(
      name=name).first()
  if price > 10:
    print("Too expensive")
  else:
    product_object.price = price
    session.commit()


def delete_product(id):
  session.query(Product).filter_by(
    id= id).delete()
  session.commit()


def get_product(id):
  pass

# create_product("test02", 20,10,"test123")
# delete_product(2)
update_product("test", 11)


