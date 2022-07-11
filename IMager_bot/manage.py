import os
import sys
import settings.command_exceptions as cexc
import importlib


def execute_from_command_line(args):
    cmds = [filename[:-3]
            for filename in os.listdir('IMager_bot/commands')
            if filename[0] != '_']
    if len(args) != 2:
        raise cexc.WrongQuantityParams('Call this file like: '
                                       'python manage.py <command>.\n'
                                       f'Commands: {cmds}')
    command = args[1]
    if command not in cmds:
        raise cexc.UnknownCommand(f'Choose from : {cmds}')
    importlib.import_module(f'commands.{command}')


if __name__ == '__main__':
    execute_from_command_line(sys.argv)    
