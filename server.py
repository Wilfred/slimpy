#!/usr/bin/env python

import traceback


def eval_line(line):
    try:
        # If it's a single statement, eval, so we have a
        # proper result.
        code_obj = compile(line, '<string>', 'eval')
    except SyntaxError:
        code_obj = compile(line, '<string>', 'exec')

    return eval(code_obj)


def command_loop():
    while True:
        line = input("user> ")
        try:
            print(eval_line(line))
        except KeyboardInterrupt:
            return
        except:
            traceback.print_exc()


if __name__ == '__main__':
    command_loop()
