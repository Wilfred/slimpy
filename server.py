#!/usr/bin/env python

import re
import traceback
from importlib import import_module


def eval_line(line):
    try:
        # If it's a single statement, eval, so we have a
        # proper result.
        code_obj = compile(line, '<string>', 'eval')
    except SyntaxError:
        code_obj = compile(line, '<string>', 'exec')

    return eval(code_obj)


def extract_module(line):
    """
    
    >>> extract_module("%module foo.bar")
    "foo.bar"
    >>> extract_module("anything else")
    None

    """
    match = re.fullmatch(r"%mod ([a-zA-Z0-9_.]+)", line)
    if match:
        return match.group(1)


def command_loop():
    module_name = "user"
    modules = {}

    while True:
        line = input("{}> ".format(module_name))

        if line == '%mod':
            print(modules)
            continue

        if line.startswith('%mod'):
            new_module_name = re.fullmatch(r"%mod ([a-zA-Z0-9_.]+)", line).group(1)
            module = import_module(new_module_name)
            modules[new_module_name] = module
            
            module_name = new_module_name
            continue
        
        try:
            print(eval_line(line))
        except KeyboardInterrupt:
            return
        except:
            traceback.print_exc()


if __name__ == '__main__':
    command_loop()
