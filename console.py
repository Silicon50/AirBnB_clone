#!/usr/bin/python3
"""
Module Console
"""
import cmd
import shlex
import sys
import models
import re
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNB Class"""
    prompt = '(hbnb) '
    classes = {
                'BaseModel': BaseModel,
                'Amenity': Amenity,
                'State': State,
                'Place': Place,
                'Review': Review,
                'User': User,
                'City': City
                            }

    def do_quit(self, args):
        """quit - exit the console"""
        return True

    def do_EOF(self, args):
        """Defines EOF option"""
        print()
        return True

    def emptyline(self):
        """Defines Empty option"""
        pass

    def do_create(self, args):
        """create <class_name> - create an instance of <class_name>"""
        if args:
            if args in self.classes:
                model = getattr(sys.modules[__name__], args)
                instance = model()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def do_show(self, args):
        """show <class_name> <id> - show instance using class_name & id"""
        tokens = shlex.split(args)
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            if tokens[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            else:
                instance_id = tokens[0] + "." + tokens[1]
                all_instance_dict = models.storage.all()
                if instance_id in all_instance_dict:
                    print(all_instance_dict[instance_id])
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """destroy <class_name> <id> - delete instance using class_name & id"""
        tokens = shlex.split(args)
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            if tokens[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            else:
                instance_id = tokens[0] + "." + tokens[1]
                all_instance_dict = models.storage.all()
                if instance_id in all_instance_dict:
                    del all_instance_dict[instance_id]
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """all, all <class_name> - display all instance"""
        tokens = shlex.split(args)
        instance_dict = []
        all_instance_dict = models.storage.all()
        if len(tokens) == 0:
            for key in all_instance_dict:
                str_obj = str(all_instance_dict[key])
                instance_dict.append(str_obj)
            print(instance_dict)
        else:
            if len(tokens) == 1:
                if tokens[0] not in self.classes:
                    print("** class doesn't exist **")
                else:
                    for key in all_instance_dict:
                        query = key.split(".")
                        if query[0] == tokens[0]:
                            str_obj = str(all_instance_dict[key])
                            instance_dict.append(str_obj)
                    print(instance_dict)

    def do_update(self, args):
        """update <class_name> <id> - update instance using class_name & id"""
        tokens = shlex.split(args)
        if len(tokens) == 0:
            print("** class name missing **")
        else:

            if tokens[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            elif len(tokens) == 2:
                print("** attribute name missing **")
            elif len(tokens) == 3:
                print("** value missing **")
            else:
                instance_id = tokens[0] + "." + tokens[1]
                if tokens[2] == "created_at" or tokens[2] == "updated_at":
                    return
                all_instances_dict = models.storage.all()
                try:
                    instance = all_instances_dict[instance_id]
                except KeyError:
                    print("** no instance found **")
                try:
                    attr_type = type(getattr(instance, tokens[2]))
                    tokens[3] = attr_type(tokens[3])
                except AttributeError:
                    pass
                setattr(instance, tokens[2], tokens[3])
                models.storage.save()

    def do_count(self, args):
        """retrieve the number of instances of a class"""
        tokens = shlex.split(args)
        dic = models.storage.all()
        num_instances = 0
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in dic:
                className = key.split('.')
                if className[0] == tokens[0]:
                    num_instances += 1
            print(num_instances)

    def precmd(self, args):
        """ executed just before the command line line is interpreted """
        new_args = str()
        tokens = re.split(r'[,.()"\s:}{\']+', args)
        tokens_len = len(tokens)
        try:
            if tokens[1] == "update":
                new_args = tokens[1] + " " + tokens[0]
                for i in range(2, tokens_len):
                    new_args = new_args + " " + tokens[i]
                return new_args
        except IndexError:
            pass
        class_model = args.split('.')
        if len(class_model) == 2:
            command = class_model[1].split('(')
            new_args = command[0] + " "
            new_args = new_args + class_model[0] + " "
            if len(command) == 2:
                query = command[1].split(')')
                new_args = new_args + query[0]
            return new_args
        else:
            return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()
