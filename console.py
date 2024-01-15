#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "shell >>> "
    def do_quit(self, line):
        """ Quit command to exit the program """
        return True
    def do_EOF(self, line):
            """ EOF """
            print()
            return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()           
