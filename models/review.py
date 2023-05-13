#!/usr/bin/python3
"""
This module creates a Review Class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review, Inherits from the BaseModel class.
    """
    place_id = ""
    user_id = ""
    text = ""
