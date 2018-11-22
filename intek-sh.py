#!/usr/bin/env python3
import cmd
import subprocess
import os


class LineArgument(cmd.Cmd):
    prompt = 'intek-sh$ '

    def do_pwd(self, line):
        print(os.environ['PWD'])

    def do_cd(self, path):
        if path:
            pass

    def do_printenv(self, variable):
        _dict = dict(os.environ)
        if variable:
            if variable in _dict.keys():
                print(_dict[variable])
            else:
                pass
        else:
            for keys, values in _dict.items():
                print(keys + '=' + values)

    def do_ls(self, line):
        subprocess.run(['ls', '-lA'])

    def do_cl(self, line):
        subprocess.run(['clear'])

    def do_exit(self, code):
        print('exit')
        exit()

    def emptyline(self):
        pass


def main():
    LineArgument().cmdloop()


if __name__ == '__main__':
    main()
