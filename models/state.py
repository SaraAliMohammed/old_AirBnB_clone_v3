#!/usr/bin/python3
"""Defines the State Module"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    State Class.
    Attributes:
        __tablename__: Table name.
        name (string): State name.
    """
    if models.is_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:
        name = ""
