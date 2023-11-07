#!/usr/bin/python3
"""Defines a base class for all models in the AirBnB clone"""

# Import necessary libraries
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, DateTime

# Create a base for declarative classes
Base = declarative_base()

class BaseModel:
    """
    This class represents a base model for other models to inherit from.

    Attributes:
        id (sqlalchemy String): The BaseModel id
        created_at (sqlalchemy DateTime): The datetime at creation
        updated_at (sqlalchemy DateTime): The datetime at last update
    """
    # Define class attributes
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if (not kwargs or 'id' not in kwargs):
            from models import storage
            # Generate a unique ID and set creation/update times
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            if kwargs:
                for k, v in kwargs.items():
                    setattr(self, k, v)
            self.save()
        else:
            # Convert date strings to datetime objects
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Saves the current instance of the BaseModel to the database.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        try:
            del dictionary['_sa_instance_state']
        except Exception:
            pass
        return dictionary

    def delete(self):
        """
        Deletes the current instance of the BaseModel from the database.
        """
        storage.delete(self)

