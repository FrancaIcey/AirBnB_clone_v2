#!/usr/bin/python3
"""Defines the State class."""
import models  # Import the 'models' module
# Import the 'getenv' function from 'os'
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    # Define the MySQL table name for States
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # Define a relationship with the 'City' class, back reference, and cascade behavior

    cities = relationship("City",  backref="state", cascade="delete")
    
    # Check the storage type
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            # Return the list of related City objects
            return city_list  
