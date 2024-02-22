#!/usr/bin/python3
'''This module defines a class to manage database storage for hbnb clone'''
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models


class DBStorage:
    '''This class manages storage of hbnb models in a SQL database'''
    __engine = None
    __session = None

    def __init__(self):
        '''Intialize DBStorge object'''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(
                                        getenv("HBNB_MYSQL_USER"),
                                        getenv("HBNB_MYSQL_PWD"),
                                        getenv("HBNB_MYSQL_HOST"),
                                        getenv("HBNB_MYSQL_DB"),
                                        pool_pre_ping=True))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        '''
        Query on the current database session
        Returns: all objects depending of the class name (argument cls),
                if cls=None,  query all types of objects
                (User, State, City, Amenity, Place and Review)
        '''
        objects = dict()
        classes = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for class_type in classes:
                query = self.__session.query(class_type)
                for obj in query.all():
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        else:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for obj in query.all():
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        '''Add the object to the current database session'''
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        '''Commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Delete from the current database session obj if not None'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''Create all tables in the database (feature of SQLAlchemy)
         scoped_session - to make sure your Session is thread-safe'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the storage engine."""
        self.__session.close()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or None if not
        found
        """
        objects = self.__session.query(cls)
        for obj in objects:
            if obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        '''
        Count the number of objects in storage.
        Args:
            cls: class (optional).
        Returns:
            The number of objects in storage matching the given class.
            If no class is passed, returns the count of all objects in storage.
        '''
        if cls is None:
            counts = 0
            classes = (User, State, City, Amenity, Place, Review)
            for class_type in classes:
                counts += self.__session.query(class_type).count()
            return counts
        else:
            return self.__session.query(cls).count()
