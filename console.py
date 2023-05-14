#!/usr/bin/python3
"""
The entry point of our command interpreter
"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(args):
    """
    Defines the pares method.
    """
    braces = re.search(r"\{(.*?)\}", args)
    brackets = re.search(r"\[(.*?)\]", args)
    if braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(args)]
        else:
            lexer = split(args[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand implements the console for AirBnB clone web app.
    """

    prompt = "(hbnb) "
    __classes_allowed = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """An empty line + ENTER shouldn't execute anything."""
        pass

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF to exit the program."""
        print("")
        return True

    def do_create(self, args):
        """Create a new instance of BaseModel.
        saves it to the JSON file
        prints the id
        Usage: create <class>"""

        argl = parse(args)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes_allowed:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, args):
        """Prints the string rep of an instance based on
        the class name and id.
        Usage: show <class name> <id>"""
        argl = parse(args)
        objects_dict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes_allowed:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objects_dict:
            print("** no instance found **")
        else:
            print(objects_dict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file).
        Usage: destroy <class name> <id>"""
        argl = parse(args)
        objects_dict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes_allowed:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objects_dict.keys():
            print("** no instance found **")
        else:
            del objects_dict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based
        on class name.
        If no class specified, display all instantiated objs.
        Usage: all <class name> or Usage: all
        """
        argl = parse(args)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes_allowed:
            print("** class doesn't exist **")
        else:
            obj_l = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    obj_l.append(obj.__str__())
                elif len(argl) == 0:
                    obj_l.append(obj.__str__())
            print(obj_l)

    def do_count(self, args):
        """
        retrieve the number of instances of a class.
        """
        argl = parse(args)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, args):
        """Updates an instance based on class name and id by adding or
        updateing attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        argl = parse(args)
        objects_dict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes_allowed:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objects_dict.keys():
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
            obj = objects_dict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = value_type(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objects_dict["{}.{}".format(argl[0], argl[1])]
            for key, value in eval(argl[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in
                        {str, int, float}):
                    value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
