#!/usr/bin/env python3
"""Propósito: Dizer oi"""


import argparse

def get_args():
    """
    Get the command-line arguments
    """
    parser = argparse.ArgumentParser(description='Say hello') #description of the program
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet') #argument of the program
    return parser.parse_args()

def main():
    """
    main
    """
    args = get_args()
    name = args.name
    print('Hello, ' + args.name + '!')

if __name__ == '__main__':
    main()
