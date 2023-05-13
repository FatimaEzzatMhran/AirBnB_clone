#!/usr/bin/python3
"""
This module creates a City Class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City, Inherits from the BaseModel class.
    """
    state_id = ""
    name = ""
