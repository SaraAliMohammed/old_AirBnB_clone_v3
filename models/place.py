#!/usr/bin/python3
"""Defines the Place Module"""
from models.base_model import BaseModel, Base
from models.amenity import Amenity
import models
from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table


if models.is_type == "db":
    relationship_table = Table('place_amenity', Base.metadata,
                               Column('place_id', String(60),
                                      ForeignKey('places.id'),
                                      nullable=False),
                               Column('amenity_id', String(60),
                                      ForeignKey('amenities.id'),
                                      nullable=False))


class Place(BaseModel, Base):
    """
    Place class.
    Attributes:
        city_id (string): City id.
        user_id (string): User id.
        name (string): Place name.
        description (string): Place description.
        number_rooms (integer): Place number of rooms.
        number_bathrooms (integer): Place number of pathrooms.
        max_guest (integer): Place maximum number of guests.
        price_by_night (integer): Place price by night.
        latitude (float): Place latitude value.
        longitude (float): Place longitude value.
        amenity_ids (list:string): Place list of amenity ids.
    """
    if models.is_type == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship('Amenity', secondary=relationship_table,
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Place reviews """
            reviews = models.storage.all(Review).values()
            return {rev for rev in reviews if rev.place_id == self.id}

        @property
        def amenities(self):
            """ Place amenities """
            ams = models.storage.all(Amenity).values()
            return [am for am in ams if am.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """ Amenities setter """
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
