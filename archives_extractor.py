#!/usr/bin/env python
# coding: utf-8

import argparse

EXT_ARCHIVERS = ['.zip', '.rar', '.bz2', '.gz', '.tar', '.tbz2', '.tgz', '.Z',
                 '.7z', '.xz', '.exe', '.tar.bz2', '.tar.gz', '.tar.xz',
                 '.arj', '.cab', '.chm', '.deb', '.dmg', '.iso', '.lzh',
                 '.msi', '.rpm', '.udf', '.wim', '.xar'] 

def grooming_list_files(lst_files):
    return lst_files
    

def archives_extractor(lst_files):
    print(lst_files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', nargs='+',
                        help='Type path of the different files to extract',
                        required=True)
    args = parser.parse_args()
    args.file = grooming_list_files(args.file)
    archives_extractor(args.file)
