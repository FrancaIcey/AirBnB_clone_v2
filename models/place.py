#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship
import os

class Place(BaseModel, Base):
    """ A place to stay """
    
    # Define the name of the database table
    __tablename__ = "places"
    
    # Place attributes
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False, default=0)
    longitude = Column(Float, nullable=False, default=0)
    
    # Amenity IDs will be stored as a list
    amenity_ids = []
    
    # Define relationships with other classes based on storage type
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="all, delete")
    else:
        @property
        def reviews(self):
            """
            Gets a list of all reviews associated with the place

            Returns:
                A list of Review objects associated with this Place
            """
            from models import storage, Review

            reviews_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

