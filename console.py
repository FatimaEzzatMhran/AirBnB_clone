#!/usr/bin/python3
"""
The entry point of our command interpreter.
"""

import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand implements the console for AirBnB clone web app.
    """

    prompt = "(hbnb) "

    allowed_classes = ["BaseModel"]

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
