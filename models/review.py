#!/usr/bin/python3
"""Defines the Review Class"""
from models.base_model import BaseModel, Base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String
import models


class Review(BaseModel, Base):
    """
    Review class.
    Attributes:
        place_id (string): Place id.
        user_id (string): User id.
        text (string): Review text
    """
    if models.is_type == "db":
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
