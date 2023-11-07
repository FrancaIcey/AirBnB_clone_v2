#!/usr/bin/python3
"""Defines the BaseModel class."""

import models  # Import the 'models' module
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

Base = declarative_base()

class BaseModel:
    """Defines the BaseModel class.

    Attributes:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """

    # Define 'id' column with constraints
    id = Column(String(60), primary_key=True, nullable=False)  
    # Define 'created_at' column with default value
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    # Define 'updated_at' column with default value
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        # Generate a unique ID
        self.id = str(uuid4())
        # Set creation and update time to current time
        if kwargs:
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")  # Convert string to datetime
                if key != "__class__":
                    # Set attributes from kwargs
                    setattr(self, key, value)

    def save(self):
        """Update updated_at with the current datetime, add instance to storage, and save storage."""
        self.updated_at = datetime.utcnow()
        # Add the instance to storage
        models.storage.new(self)
        # Save the storage
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        my_dict = self.__dict__.copy()
        # Add '__class__' to dictionary
        my_dict["__class__"] = str(type(self).__name__)
        # Convert 'created_at' to ISO format string
        my_dict["created_at"] = self.created_at.isoformat()
        # Convert 'updated_at' to ISO format string
        my_dict["updated_at"] = self.updated_at.isoformat()
        # Remove SQLAlchemy instance state
        return my_dict
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def delete(self):
        """Delete the current instance from storage."""
        # Delete the instance from storage
        models.storage.delete(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__.copy()
        # Remove SQLAlchemy instance state
        d.pop("_sa_instance_state", None)
        # Format a string representation
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
