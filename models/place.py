#!/usr/bin/python3
"""Defines the Place class."""
import models  # Import the 'models' module
from os
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Float, ForeignKey, String, Table, Integer 
from sqlalchemy.orm import relationship

# Define the association table for the Place-Amenity relationship
place_amenity_assoc = Table("place_amenity", Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """Represents a Place for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table places.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store places.
        city_id (sqlalchemy String): The place's city id.
        user_id (sqlalchemy String): The place's user id.
        name (sqlalchemy String): The name.
        description (sqlalchemy String): The description.
        num_rooms (sqlalchemy Integer): The number of rooms.
        num_bathrooms (sqlalchemy Integer): The number of bathrooms.
        max_guest (sqlalchemy Integer): The maximum number of guests.
        price_per_night (sqlalchemy Integer): The price per night.
        latitude (sqlalchemy Float): The place's latitude.
        longitude (sqlalchemy Float): The place's longitude.
        reviews (sqlalchemy relationship): The Place-Review relationship.
        amenities (sqlalchemy relationship): The Place-Amenity relationship.
        amenity_ids (list): An id list of all linked amenities.
    """
    # Define the MySQL table name for Places
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    num_rooms = Column(Integer, default=0)
    num_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_per_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary=place_amenity_assoc,
                             viewonly=False, overlaps="place_amenities")
    # Initialize an empty list for amenity IDs
    amenity_ids = []

    # Check the storage type
    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            # Return the list of linked Reviews
            return review_list

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            # Return the list of linked Amenities
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            # Check if the value is an instance of Amenity
            if isinstance(value, Amenity):
                # Add the Amenity ID to the list
                self.amenity_ids.append(value.id)
