#!/Usr/bin/python3
"""test_base_model module"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ test class for BaseModel class """

    def setUp(self):
        """setting up"""
        self.model = BaseModel()

    def tearDown(self):
        """ clean up """
        self.model = None

    def test_BaseModel_docstring(self):
        """testing if BaseModel has comment"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_model_type(self):
        """testing for module existenc"""
        self.assertIsInstance(self.model, BaseModel)

    def test_model_attributes(self):
        """testing if model attributes are set and are of expected type"""
        self.assertEqual(type(self.model.id).__name__, "str")
        self.assertTrue(isinstance(self.model.created_at, datetime))
        self.assertTrue(isinstance(self.model.updated_at, datetime))

    def test__str__docstring(self):
        """testing if __str__ contians a comment"""
        self.assertIsNotNone(self.model.__str__.__doc__)

    def test__str__(self):
        """ testing for the string representation """
        form = "[{}] ({}) {}"
        instance_class = self.model.__class__.__name__
        instance_id = self.model.id
        instance_dict = self.model.__dict__
        self.dic = form.format(instance_class, instance_id, instance_dict)
        self.assertEqual(self.dic, str(self.model))

    def test_save_doctstring(self):
        """testing if save() method has a comment"""
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_save_updated_at(self):
        """
        testing for the updated value of updated_at attribute
        when save() method is called on the object
        """
        self.temp_date = self.model.updated_at
        self.assertEqual(self.temp_date, self.model.updated_at)
        self.model.save()
        self.assertNotEqual(self.temp_date, self.model.updated_at)

    def test_save_created_at(self):
        """
        testing for the updated value of created_at attribute
        when save() method is called on the object
        """

        self.temp_date = self.model.created_at
        self.assertEqual(self.temp_date, self.model.created_at)
        self.model.save()
        self.assertEqual(self.temp_date, self.model.created_at)

    def test_to_dict_is_returned(self):
        """
        checking id dictionary object is returned
        when to_dict() method is called on model
        """
        instance_dict = self.model.to_dict()
        self.assertIsInstance(instance_dict, dict)

    def test_to_dict_none(self):
        """test if the returned dictionary from to_dict() is None type"""
        instance_dict = self.model.to_dict()
        self.assertIsNotNone(instance_dict)

    def test_to_dict_create_at(self):
        """
        test if the returned dictionary from
        to_dict() attribute create_at is of
        string type
        """
        instance_dict = self.model.to_dict()
        self.assertIsInstance(instance_dict["created_at"], str)

    def test_to_dict_updated_at(self):
        """
        test if the returned dictionary from
        to_dict() attribute updated_at is of
        string type
        """
        instance_dict = self.model.to_dict()
        self.assertIsInstance(instance_dict["updated_at"], str)

    def test_to_dict_attr_class(self):
        """
        testing if the attribute __class__ of returned dictionary
        by to_dict() is present
        """
        instance_dict = self.model.to_dict()
        self.assertIn("__class__", instance_dict)


if __name__ == '__main__':
    unittest.main()
