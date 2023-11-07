#!/usr/bin/python3
"""City Module for HBNB project"""

# Import necessary libraries and classes
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """
    City class for storing city data.

    Attributes:
        __tablename__ (str): The name of the database table to store city data.
        state_id (sqlalchemy.Column): The ID of the state that this city
                                      belongs to, stored as a string.
        name (sqlalchemy.Column): The name of the city, stored as a string.
        places (relationship): One-to-Many relationship with the Place class,
                              back-referenced as "cities", with cascade delete.
    """
    # Define the name of the database table
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")
