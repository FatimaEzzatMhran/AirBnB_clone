#!/usr/bin/python3
"""
Module for the base class of all our models.
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel class.

        Arguments:
            - *args: list of non keyword arguments.
            - **kwargs: dictionary of keyword arguments.
        """

        from models import storage
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformate(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Returns the string representation of BaseModel object.
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attr updated_at with the current datetime.
        """

        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance:
            - only instance attributes set will be returned
            - a key __class__ must be added to this dictionary
            - created_at & updated_at converted to string object in ISO format
        """

        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
                mydict[key] = value
        return mydict
