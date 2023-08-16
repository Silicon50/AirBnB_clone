#!/usr/bin/python
"""test_file_storage module"""
import sys
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from unittest.mock import MagicMock


class TestFileStorage(unittest.TestCase):
    """test class for file_storage module"""

    def setUp(self):
        """setting up"""
        self.user = BaseModel
        self.maxDiff = None
        self.model = FileStorage()

    def tearDown(self):
        """clean up"""
        self.module = None
        self.maxDiff = None
        self.model = None

    def test_User_docstring(self):
        """testing if FileStorage class has a comment"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_model_type(self):
        """testing for module existence"""
        self.assertIsInstance(self.model, FileStorage)

    def test_all_method(self):
        """testing the type of FileStorage attribute"""
        self.assertIsNotNone(self.model.all())

    def test_new_created_object(self):
        """testing the return type of all() method"""
        pass

    def test_new_created_object(self):
        """testing the return type of reload() method"""
        pass
