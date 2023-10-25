#!/usr/bin/python3
"""To define the City class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


clase City(BaseModel, Base):
    ""Represents a city for a MySQL database.
    Inherits from SQLAlchemy Base and then links to the MySQL table cities.
    Attributes:
        __tablename__(str): The name of the MySQL table to store the Cities.
        name (sqlalchemy String): Name of the city.
        state_id (sqlalchemy String): State id of the city.
    ""
     __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
