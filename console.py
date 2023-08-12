#!/usr/bin/python3
"""DEfine the HBnB Console"""

import cmd
import re
import importlib
from models import storage
from shlex import split

class HBNBCommand(cmd.Cmd):
    """HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel", "User", "State", "City", "Place", "Amenity", "Review"
    }

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def default(self, arg):
        """Handles unknown syntax."""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict:
                    call = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        arg_list = [i.strip(",") for i in split(arg)]
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg_list[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Display the string representation of a class instance of a given id."""
        arg_list = [i.strip(",") for i in split(arg)]
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            obj_id = "{}.{}".format(arg_list[0], arg_list[1])
            if obj_id in storage.all():
                print(storage.all()[obj_id])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""
        arg_list = [i.strip(",") for i in split(arg)]
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            obj_id = "{}.{}".format(arg_list[0], arg_list[1])
            if obj_id in storage.all():
                storage.all().pop(obj_id)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Display string representations of all instances of a given class."""
        arg_list = [i.strip(",") for i in split(arg)]
        obj_list = []
        if not arg_list:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        elif arg_list[0] in self.classes:
            for obj in storage.all().values():
                if obj.__class__.__name__ == arg_list[0]:
                    obj_list.append(str(obj))
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        arg_list = [i.strip(",") for i in split(arg)]
        count = 0
        if not arg_list:
            print("** class name missing **")
            return
        elif arg_list[0] in self.classes:
            for obj in storage.all().values():
                if obj.__class__.__name__ == arg_list[0]:
                    count += 1
        else:
            print("** class doesn't exist **")
            return
        print(count)

    def do_update(self, arg):
        """Update a class instance of a given id by adding or updating attributes."""
        arg_list = [i.strip(",") for i in split(arg)]
        obj_dict = storage
