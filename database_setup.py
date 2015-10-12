import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlaclhemy.ext.declarative import devlarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):

    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):

    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

engine = create)engine('sqlite:///restaurant.db')



Base.metadata.create_all(engine)
