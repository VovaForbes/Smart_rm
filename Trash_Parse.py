import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-re", "--restore", nargs='+', help="Restore the files with the according names from the bucket")
parser.add_argument("-l", "--list", type=int, help="Show the list of items in our bucket")
parser.add_argument("-c", "--clear", help="clears the bucket")

args = parser.parse_args()

list_to_restore = []
clear_ = False
list_ = 0

if args.restore:
    for name in args.restore:
        list_to_restore.append(name)

if args.clear:
    clear_ = True

if args.list:
    list_ = args.list
