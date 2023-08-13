#!/usr/bin/python3

"""A Basemodel that defines all other classes """
import uuid
from datetime import datetime


class BaseModel():
    """A base class that define common attributes and methods of other classes
    Attribute:
        id : string - returns a unique identifier when an instance is created
        created_at : datetime - assign current datetime
        updated_at : datetime - assign with current datetime
    Public Instance Methods :
        save : update update_at with current datetime
        to_dict : returns a dictionay containing all keys/value of the instance
    """

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """Initializing the basemodel"""
        if len(kwargs) != 0:
            for key, value in kwargs.item():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """The string representation of the object"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """A method used to update the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict keys/values of __dict__ of the instance"""
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
