#!/usr/bin/python3
"""Creating a new engine 'DBStorage'"""

import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """Represents a database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializing new instance in db"""
        # Fix the connection string to include all parameters
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                                      .format(os.environ.get('HBNB_MYSQL_USER'),
                                              os.environ.get('HBNB_MYSQL_PWD'),
                                              os.environ.get('HBNB_MYSQL_HOST'),
                                              3306,  # Port
                                              os.environ.get('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Initialize the session
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        # Define a list of classes to query
        classes_to_query = [cls] if cls else [User, State, City, Amenity, Place, Review]

        # Initialize a dictionary to store the results
        results = {}

        # Query objects for each class in the list
        for class_name in classes_to_query:
            objects = self.__session.query(class_name).all()

            # Populate the results dictionary using a dictionary comprehension
            results.update({f"{class_name.__name__}.{obj.id}": obj for obj in objects})

        return results

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize the session"""
        Base.metadata.create_all(self.__engine)

