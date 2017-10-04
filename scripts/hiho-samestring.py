#!/usr/bin/env python3
import argparse
import glob
import os

description = """"show the sets of 2 strings. string can input strings or glob or string file."""

parser = argparse.ArgumentParser(description=description)
parser.add_argument('-1', '--strings_1', nargs='+', required=True)
parser.add_argument('-2', '--strings_2', nargs='+', required=True)
parser.add_argument('-ed', '--eliminate_directory', action='store_true', help="eliminate directory")
parser.add_argument('-ee', '--eliminate_extension', action='store_true', help="eliminate extension")
parser.add_argument('-o1', '--show_only_1', action='store_true', help="show names that only first have")
parser.add_argument('-o2', '--show_only_2', action='store_true', help="show names that only second have")
parser.add_argument('-b', '--show_both', action='store_true', help="show names that both have")
args = parser.parse_args()


def load_strings(strings):
    if len(strings) > 1:
        return strings

    path = strings[0]
    if os.path.exists(path):
        with open(path) as f:
            return f.read().split()

    else:
        return glob.glob(path)


def get_names(strs, eliminate_directory, eliminate_extension):
    if eliminate_directory:
        strs = (os.path.basename(n) for n in strs)
    if eliminate_extension:
        strs = (os.path.splitext(n)[0] for n in strs)
    return set(strs)


names1 = get_names(load_strings(args.strings_1), args.eliminate_directory, args.eliminate_extension)
names2 = get_names(load_strings(args.strings_2), args.eliminate_directory, args.eliminate_extension)

print('num of first:', len(names1))
print('num of second:', len(names2))
print('num of both contained:', len(names1 & names2))

if args.show_only_1:
    print('only first:')
    for n in (names1 - names2):
        print(n)

if args.show_only_2:
    print('only second:')
    for n in (names2 - names1):
        print(n)

if args.show_both:
    print('both:')
    for n in (names2 & names1):
        print(n)
