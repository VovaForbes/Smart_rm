import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--remove", nargs="+", help="Remove some files and directories that are listed in arguments")
parser.add_argument("-re", "--regexp_r", nargs="+", help="Delete by some regular expression")

args = parser.parse_args()

list_remove = []
list_remove_regex = []

if args.remove:
    for name in args.remove:
        list_remove.append(name)

if args.regexp_r:
    for name in args.regexp_r:
        list_remove_regex.append(name)

