#!/usr/bin/env python3
"""
Author : whoami <whoami@localhost>
Date   : 2025-02-09
Purpose: Picnic game
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s', '--sorted', action='store_true',
                        help='Sort the items')

    return parser.parse_args()


def main():
    """Present day, present time"""

    args = get_args()
    items = args.str

    if args.sorted:
        items.sort()

    if not items:
        print("You must provide a list of items to bring.")
    elif len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print(f'You are bringing {bringing}.')


if __name__ == '__main__':
    main()
