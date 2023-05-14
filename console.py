#!/usr/bin/python3
"""
The entry point of our command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand implements the console for AirBnB clone web app.
    """

    prompt = "(hbnb) "
    storage = FileStorage()

    allowed_classes = ["BaseModel",
                       "User",
                       "State",
                       "City",
                       "Amenity",
                       "Place",
                       "Review"]

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the console."""
        print("")
        return True

    def do_create(self, args):
        """Create a new instance of BaseModel.
        saves it to the JSON file
        prints the id
        Usage: create <class>"""

        args = args.split()
        if len(args) != 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(args[0])()
            print(new_object.id)
            new_object.save()

    def do_show(self, args):
        """Prints the string rep of an instance based on
        the class name and id.
        Usage: show <class name> <id>"""

        args = args.split()
        objects_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in objects_dict:
            print("** no instance found **")
        else:
            print(objects_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file).
        Usage: destroy <class name> <id>"""

        args = args.split()
        objects_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in objects_dict:
            print("** no instance found **")
        else:
            del objects_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based
        on class name.
        If no class specified, display all instantiated objs.
        Usage: all <class name> or Usage: all
        """

        args = args.split()
        if len(args) > 0 and args[0] not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
        else:
            objects_list = []
            for obj in storage.all().values:
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objects_list.append(obj.__str.__())
                if len(args) == 0:
                    objects_list.append(obj.__str.__())
            print(objects_list)

    def do_update(self, args):
        """Updates an instance based on class name and id by adding or
        updateing attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = args.split()
        objects_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objects_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = objects_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = value_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objects_dict["{}.{}".format(args[0], args[1])]
            for key, value in eval(args[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in
                        {str, int, float}):
                    value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
