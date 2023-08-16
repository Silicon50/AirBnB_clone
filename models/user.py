#!/usr/bin/python3
from models.base_model import BaseModel
"""user model"""


class User(BaseModel):
    """ Class user that inherits from base_model """

    email = str()
    password = str()
    first_name = str()
    last_name = str()
