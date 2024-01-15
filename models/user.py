#!/usr/bin/python3
"""Defines the User Class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class User(BaseModel, Base):
    """
    Class that contains all user information.
    Attributes:
        email (string): User email.
        password (string): User password.
        first_name (string): User first name.
        last_name (string): User last name.
    """
    if models.is_type == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', backref='user', cascade='delete')
        reviews = relationship('Review', backref='user', cascade='delete')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
