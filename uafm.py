#!/usr/bin/env python
# coding: utf-8
import sys
import subprocess
import mimetypes
import click
from shutil import which

from operator import itemgetter

from config import TOOLS

import pathlib


COMPACT = "compact"
EXTRACT = "extract"

DEFAULT_ARCHIVE_NAME = "archive.tar"
MIME = mimetypes.MimeTypes()

@click.group()
def uafm():
    pass


def _process(name, sources, dest, clean):
    mime_type = MIME.guess_type(dest)[0] if name == COMPACT else MIME.guess_type(sources[0])[0]
    package, options, pattern = itemgetter("package", "options", "pattern")(TOOLS[mime_type][name])
    if which(package) is None:
        sys.exit(f'command not found: {package}')
    command_line = pattern.format(package=package, options=options, sources=' '.join(map(str, sources)), destination=dest)
    subprocess.run(command_line, check=True, shell=True)


def _rm_sources(sources):
    subprocess.run(["rm", "-r", *sources], check=True, shell=True)


@uafm.command(name=COMPACT)
@click.argument('sources', nargs=-1, type=click.Path(exists=True), required=True) # , help='List of elements to compact'
@click.option('--dest', nargs=1, type=click.Path(exists=False), default=DEFAULT_ARCHIVE_NAME) # , help="Path where store the output"
@click.option('--clean', type=bool, default=False) # , help="Clean source after operation"
def compact(sources, dest, clean):
    _process(COMPACT, sources, dest, clean)

    if (clean):
        _rm_sources(sources)


@uafm.command(name=EXTRACT)
@click.argument('sources', nargs=-1, type=click.Path(exists=True), required=True) # , help='List of elements to extract'
@click.option('--dest', nargs=1, type=click.Path(exists=True)) # , help="Path where store the output"
@click.option('--clean', type=bool, default=False) # , help="Clean source after operation"
def extract(sources, dest, clean):
    for source in sources:
        _process(EXTRACT, [source], dest, clean)
    
    if (clean):
        _rm_sources(sources)


@click.command(cls=click.CommandCollection, sources=[uafm])
def cli():
    pass


if __name__ == '__main__':
    # Universal Archive Files Manager (UAFM)
    # program_name: uafm
    # Usage:
    # uafm <archive> | uafm extract <archive> => extract/decompress an archive in the current directory (pwd)
    # uafm <archive> --dest <dir> | uafm extract <archive> --dest <dir> => extract/decompress an archive in a specified directory
        # - if the path to the specified directory doesn't exist, create it
    # uafm compact <files> => archive/compress a list of files in the current directory (pwd)
    # uafm compact <files> --dest <dir> => archive/compress a list of files in the current directory (pwd)
    
    # Prototype
    # <program_name> <command> <sources> <destination>
    # program_name = uafm
    # command: ["extract", "compact"]
    # sources: with extract command an archive ; with compact command a list of files
    # destination: with extract command an archive, path where store the output ; with compact operation the path of the creating archive
    cli()