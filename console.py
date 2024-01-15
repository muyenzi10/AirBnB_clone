#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_quit(self, x):
        """ Quit command to exit the program """
        return True
    def do_EOF(self, x):
            """ EOF """
            print()
            return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()                      
