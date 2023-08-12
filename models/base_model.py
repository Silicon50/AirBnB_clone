#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class that defines common attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel Instance.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes for recreating the instance
        """
        if kwargs:
            self.deserialize(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def deserialize(self, kwargs):
        """
        Re-create an instance using a dictionary representation.

        Args:
            kwargs (dict): Dictionary containing key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = kwargs.get("id", str(uuid4()))
        self.created_at = datetime.strptime(kwargs.get("created_at", ""), tform)
        self.updated_at = datetime.strptime(kwargs.get("updated_at", ""), tform)
        for key, value in kwargs.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(self, key, value)

    def save(self):
        """
        Update updated_at with the current datetime and save to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        return {
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    def __str__(self):
        """
        Return the print/str representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
