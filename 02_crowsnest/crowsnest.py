#!/usr/bin/env python3
"""
Author : lubuntu <lubuntu@localhost>
Date   : 2024-07-21
Purpose: Crow's nest program
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crows Nest',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A word')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.positional
    vogais = ("a", "e", "i", "o", "u")
    if word.lower().startswith(vogais):
        article = "an"
    else:
        article = "a"
    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")

# --------------------------------------------------
if __name__ == '__main__':
    main()
