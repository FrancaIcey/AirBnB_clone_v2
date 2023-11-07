#!/usr/bin/python3
"""Module defining a User class for the HBNB project"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user with various attributes"""

    # Define the name of the database table
    __tablename__ = "users"
    
    # User attributes
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Define relationships with other classes
    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
