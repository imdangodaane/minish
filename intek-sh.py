#!/usr/bin/env python3
import argparse
import cmd
import subprocess


def argument():
    parser = argparse.ArgumentParser(description='built-in parser')


class LineArgument(cmd.Cmd):
    prompt = 'intek-sh$ '
    def do_ls(self, person):
        subprocess.run(['ls', '-la'])

    def do_exit(self, line):
        exit()


def basic_loop():
    while True:
        inp = str(input('intek-sh$ '))


def main():
    basic_loop()


if __name__ == '__main__':
    LineArgument().cmdloop()
