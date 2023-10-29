#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), Nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), Nullable=False, ForeignKey('uses.id'))
    name = Column(String(128), Nullable=False)
    description = Column(String(1024), Nullable=True)
    number_rooms = Column(Integer, Nullable=False, Default=0)
    number_bathrooms =  Column(Integer, Nullable=False, Default=0)
    max_guest =  Column(Integer, Nullable=False, Default=0)
    price_by_night =   Column(Integer, Nullable=False, Default=0)
    latitude =  Column(Float, Nullable=True)
    longitude =  Column(Float, Nullable=True)
    amenity_ids = []
