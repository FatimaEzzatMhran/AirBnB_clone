#!/usr/bin/python3
"""
This module creates a User Class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User, Inherits from the BaseModel class.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
