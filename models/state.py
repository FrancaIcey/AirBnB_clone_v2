#!/usr/bin/python3
""" State Module for HBNB project """

# Import necessary libraries and classes
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os

class State(BaseModel, Base):
    """
    State class for storing state data.

    Attributes:
        __tablename__ (str): The name of the database table to store
                            state data.
        name (sqlalchemy.Column): The name of the state, stored as a string.
        cities (relationship): One-to-Many relationship with the City class,
                              back-referenced as "state", with cascade delete.
    """

    # Define the name of the database table
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """
            Get a list of all cities associated with this state.

            Returns:
                A list of City objects associated with this state.
            """
            from models import storage, City

            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
