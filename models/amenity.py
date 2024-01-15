#!/usr/bin/python3
"""Defines the Amenity Module"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
    Amenity Class.
    Attributes:
        name (string): Amenity name.
    """
    if models.is_type == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
