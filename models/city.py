#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

     # Table name is set to 'cities'
    __tablename__ = "cities"

    # Column for city names, not nullable
    name = Column(String(128), nullable=False)

    # Column for state ID, a foreign key to states.id, not nullable
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

