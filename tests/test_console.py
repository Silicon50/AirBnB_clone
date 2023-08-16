#!/usr/bin/python3
"""
    test_console module for the implementation of
    unittest for console module
"""
import sys
import unittest
import models
from io import StringIO
from unittest.mock import patch, mock_open, create_autospec
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """ test class for console nodule"""

    def setUp(self):
        """set up"""
        self.console = HBNBCommand()
        self.output = StringIO()
        self.no_class_name = "** class name missing **\n"
        self.class_not_exist = "** class doesn't exist **\n"
        self.no_id = "** instance id missing **\n"
        self.no_instance = "** no instance found **\n"
        self.no_attribute = "** attribute name missing **\n"
        self.no_value = "** value missing **\n"

    def tearDown(self):
        """clean up"""
        self.console = None
        self.output = None
        self.no_class_name = None
        self.class_not_exist = None
        self.no_id = None
        self.no_instance = None
        self.no_attribute = None
        self.no_value = None

    def test_quit(self):
        """testing for the presence of quit command"""
        self.assertTrue(hasattr(self.console, "do_quit"))

    def test_help_quit_command(self):
        """testing help command on quit command"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('help quit')
        captured_output = self.output.getvalue()
        self.assertIsNotNone(captured_output)

    def test_quit_command(self):
        """testing if the quit command is executed"""
        with patch('sys.stdout', new=self.output):
            self.assertTrue(self.console.onecmd('quit'))

    def test_quit_with_argument(self):
        """testing if the exit command is executed with argument"""
        with patch('sys.stdout', new=self.output):
            self.assertTrue(self.console.onecmd('quit User'))

    def test_create(self):
        """testing for the presence create command"""
        self.assertTrue(hasattr(self.console, "do_create"))

    def test_help_create_command(self):
        """testing help command on create command"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('help create')
        captured_output = self.output.getvalue()
        self.assertIsNotNone(captured_output)

    def test_create_no_class_name(self):
        """testing create command with no class name"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('create')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.no_class_name)

    def test_create_correct_class_name(self):
        """testing create command with correct class name"""
        temp1 = StringIO()
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('create User')
        captured_output = self.output.getvalue()
        with patch('sys.stdout', new=temp1):
            self.console.onecmd('show User' + captured_output)
        temp_output = temp1.getvalue()
        self.assertNotEqual(temp_output, self.no_instance)

    def test_create_wrong_class_name(self):
        """testing create command with wrong class name"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('create user')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.class_not_exist)

    def test_show(self):
        """testing for the presence of show command"""
        self.assertTrue(hasattr(self.console, "do_show"))

    def test_help_show_command(self):
        """testing help command on show command"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('help show')
        captured_output = self.output.getvalue()
        self.assertIsNotNone(captured_output)

    def test_show_no_class_name(self):
        """testing show command with no class name"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('show')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.no_class_name)

    def test_show_correct_class_name_only(self):
        """testing show command with class name only"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('show User')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.no_id)

    def test_show_correct_class_name_wrong_id(self):
        """testing show command with class name & wrong id"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('show User 8454838-534245-252424')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.no_instance)

    def test_show_wrong_class_name(self):
        """testing show command with wrong class name"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('show user')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.class_not_exist)

    def test_all(self):
        """testing for the presence of all command"""
        self.assertTrue(hasattr(self.console, "do_all"))

    def test_all_no_class_name(self):
        """testing with no class name"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('all')
        captured_output = self.output.getvalue()
        self.assertNotEqual(captured_output, self.no_class_name)
        self.assertIsInstance(captured_output, str)

    def test_all_correct_class_name(self):
        """testing all command with correct class name"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('all User')
        captured_output = self.output.getvalue()
        self.assertNotEqual(captured_output, self.no_class_name)
        self.assertIsInstance(captured_output, str)

    def test_all_wrong_class_name(self):
        """testing all command with wrong class name"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('all user')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.class_not_exist)

    def test_help_all_command(self):
        """testing help command on all command"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('help all')
            captured_output = self.output.getvalue()
            self.assertIsNotNone(captured_output)

    def test_update(self):
        """testing for the presence of update command"""
        self.assertTrue(hasattr(self.console, "do_update"))

    def test_update_no_class_name(self):
        """testing update command with no class name"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('update')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.no_class_name)

    def test_update_correct_class_name_only(self):
        """testing update command with class name only"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('update User')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.no_id)

    def test_update_wrong_class_name(self):
        """testing update command with wrong class name"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('update user')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.class_not_exist)

    def test_update_no_attribute(self):
        """testing update command with no attribute"""
        temp = StringIO()
        with patch('sys.stdout', new=temp):
            self.console.onecmd('create User')
        temp_out = temp.getvalue()
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('update User' + " " + temp_out)
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.no_attribute)

    def test_update_no_value(self):
        """testing update command with no value"""
        temp = StringIO()
        with patch('sys.stdout', new=temp):
            self.console.onecmd('create User')
        temp_out = temp.getvalue()
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('update User' + " " + temp_out + "name")
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.no_value)

    def test_update_successful(self):
        """tesing update commanda for successful update"""
        temp1 = StringIO()
        temp2 = StringIO()
        temp3 = StringIO()
        with patch('sys.stdout', new=temp1):
            self.console.onecmd('create User')
        temp1_out = temp1.getvalue()
        with patch('sys.stdout', new=temp2):
            self.console.onecmd('show User' + " " + temp1_out)
        temp2_out = temp2.getvalue()
        with patch('sys.stdout', new=temp3):
            self.console.onecmd('update User ' + temp1_out + "name Provo")
        temp3_out = temp3.getvalue()
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('show User' + " " + temp1_out)
        captured_output = self.output.getvalue()
        self.assertNotEqual(captured_output, temp2_out)

    def test_help_update_command(self):
        """testing help command on update command"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('help update')
        captured_output = self.output.getvalue()
        self.assertIsNotNone(captured_output)

    def test_destroy(self):
        """testing for the presence of destroy command"""
        self.assertTrue(hasattr(self.console, "do_destroy"))

    def test_destroy_no_class_name(self):
        """testing destroy command with no class name"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('destroy')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.no_class_name)

    def test_destroy_correct_class_name_only(self):
        """testing destroy command with class name only"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('destroy User')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.no_id)

    def test_detroy_wrong_class_name(self):
        """testing  destroy command with wrong class name"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('destroy user')
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.class_not_exist)

    def test_detroy_correct_class_name(self):
        """testing  destroy command with correct class name & id"""
        temp1 = StringIO()
        temp2 = StringIO()
        with patch('sys.stdout', new=temp1):
            self.console.onecmd('create User')
        temp_output = temp1.getvalue()
        with patch('sys.stdout', new=temp2):
            self.console.onecmd('destroy User ' + temp_output)
        temp2_output = temp2.getvalue()
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('show User ' + temp_output)
        captured_output = self.output.getvalue()
        self.assertEqual(captured_output, self.no_instance)

    def test_help_destroy_command(self):
        """testing help command on destroy command"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('help destroy')
        captured_output = self.output.getvalue()
        self.assertIsNotNone(captured_output)

    def test_EOF_handler(self):
        """testing for the presence of EOF handler"""
        self.assertTrue(hasattr(self.console, "do_EOF"))

    def test_help_EOf_handler(self):
        """testing help command on EOF handler"""
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('help EOF')
        captured_output = self.output.getvalue()
        self.assertIsNotNone(captured_output)

    def test_EOF_handler(self):
        """testing if EOF handler is initiated"""
        with patch('sys.stdout', new=self.output):
            self.assertTrue(self.console.onecmd('EOF'))

    def test_for_unavailable_command(self):
        """testing for the presence of EOF handler"""
        self.assertFalse(hasattr(self.console, "do_transfer"))


if __name__ == "__main__":
    unittest.main()
