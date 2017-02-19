#!/usr/bin/env python

import traceback


def command_loop():
    while True:
        line = input("user> ")
        try:
            try:
                # If it's a single statement, eval, so we have a
                # proper result.
                code_obj = compile(line, '<string>', 'eval')
            except SyntaxError:
                code_obj = compile(line, '<string>', 'exec')

            result = eval(code_obj)
            print(result)
        except KeyboardInterrupt:
            return
        except:
            traceback.print_exc()


if __name__ == '__main__':
    command_loop()
