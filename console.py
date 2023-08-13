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
        """string rep of a class instance of a given id."""
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
        """Update a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
