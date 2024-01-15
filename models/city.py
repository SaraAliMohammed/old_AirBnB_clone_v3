#!/usr/bin/python3
"""Defines the City Module"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Defines the city class.
    Attributes:
        __tablename__: Table name.
        state_id (string): State id.
        name (string): City name.
    """
    if models.is_type == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        # places = relationship('Place', backref='cities', cascade='delete')
    else:
        state_id = ""
        name = ""
