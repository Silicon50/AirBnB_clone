#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
"""file_storage module"""


class FileStorage():
    """
    attributes: __file_path, __objects
    methods:
        all() - returns the dictionary < __objects>
        save() - save dictionary objects <__objects> to a jason file
        new(obj) creates new object using <obj>, where id is {class}.{id}
        reload() - deserializes the JSON file <file.json>
                to dictionary object <__objects>
    """
    __file_path = str("file.json")
    __objects = dict()

    def all(self):
        """  returns the dictionary:  __objects """

        return self.__objects

    def new(self, obj):
        """
        creates new object, where id is <class>.<id>
        """
        self.obj = obj
        key = self.obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        save __objects dictionary to a jason file
        """
        objects = self.__objects
        obj_dict = {obj: objects[obj].to_dict() for obj in objects.keys()}
        with open(self.__file_path, "w") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        try:
            with open(self.__file_path, 'r', encoding="UTF8") as json_file:
                for key, value in json.load(json_file).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass
