#!/usr/bin/python3
"""
Module for the base class of all our models.
"""

from datetime import datetime
# import models
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

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Returns the string representation of BaseModel object.
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attr updated_at with the current datetime.
        """

        self.updated_at = datetime.now()
        # storage.save()

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance:
            - only instance attributes set will be returned
            - a key __class__ must be added to this dictionary
            - created_at & updated_at converted to string object in ISO format
        """

        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = mydict["created_at"].isoformat()
        if "updated_at" in mydict:
            mydict["updated_at"] = mydict["updated_at"].isoformat()
        return mydict
