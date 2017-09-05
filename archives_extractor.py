#!/usr/bin/env python
# coding: utf-8

import argparse
import os

ARCHIVERS = {
             '.img.gz': 'gunzip',
             '.tar.bz2': 'tar -jxvf',
             '.tar.gz': 'tar -zxvf',
             '.tar.xz': 'tar xf',
             '.arj': 'arj e',
             '.bz2': 'bzip2 -d',
             '.cab': 'cabextract -d',
             '.chm': 'archmage',
             '.deb': 'ar x',
             '.dmg': '7z x',
             '.exe': '7z e',
             '.gz': 'gzip -d',
             '.iso': '7z x',
             '.lzh': '7z x',
             '.msi': '7z x',
             '.rar': 'unrar x',
             '.rpm': 'rpm2cpio',
             '.tar': 'tar -xvf',
             '.tbz': 'tar -jxvf',
             '.tbz2': 'tar -jxvf',
             '.tgz': 'tar -xvzf',
             '.udf': '',
             '.wim': '',
             '.xar': 'xar -x',
             '.xz': 'tar xf',
             '.zip': 'unzip',
             '.Z': 'uncompress',
             '.7z': '7za x',
            }


def identify_extension(f):
    for extension in ARCHIVERS.keys():
        if extension in f:
            return extension
    print("error: file extension not found: {}".format(f))
    return None


def build_command_line(command, f):
    command_line = '{} {}'.format(command, f)
    return command_line


def execute_(command_line):
    os.system(command_line)


def archives_extractor(f):
    extension = identify_extension(f)
    if extension:
        command = ARCHIVERS[extension]
        if command:
            execute_(build_command_line(command, f))
        else:
            print("error: program not found to extract: {}".format(extension))


def main():
    args.files = list(set(args.files))
    list(map(archives_extractor, args.files))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', nargs='+',
                        help='Type path of the different files to extract',
                        required=True)
    args = parser.parse_args()
    main()
