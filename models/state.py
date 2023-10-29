#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    # Table name is set to 'states'
    __tablename__ = "states"

    # Column for city names, not nullable
    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Getter attribute for cities that returns a list of City"""
            # Import the City model if not already imported
            from models import storage, City
            # Assuming self.id is the current state's ID
            cities = [city for city in storage.all(City).values() if city.state_id == self.id]
            return cities
