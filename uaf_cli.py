#!/usr/bin/env python
# coding: utf-8
import sys
import pathlib
import subprocess
from shutil import which

import click
from operator import itemgetter

from utils import validate_filepath
from constants import CONFIG_MIME_TYPE, COMPACT, EXTRACT, DEFAULT_ARCHIVE, MIME


@click.group()
def uaf_cli():
    pass


def _process(cli_command, sources, dest, clean):
    mime_type = MIME.guess_type(dest) if cli_command == COMPACT else MIME.guess_type(sources[0])
    package, options, pattern = itemgetter("package", "options", "pattern")(CONFIG_MIME_TYPE[mime_type][cli_command])
    if which(package) is None:
        sys.exit(f'command not found: {package}')
    command_line = pattern.format(package=package, options=options, sources=' '.join(map(str, sources)), destination=dest)
    subprocess.run(command_line, check=True, shell=True)


def _rm_sources(sources):
    subprocess.run(["rm", "-r", *sources], check=True, shell=True)


@uaf_cli.command(name=COMPACT)
@click.argument('sources', nargs=-1, type=click.Path(exists=True), required=True) # , help='List of elements to compact'
@click.option('--dest', nargs=1, type=click.Path(exists=False), default=DEFAULT_ARCHIVE) # , help="Path where store the output"
@click.option('--clean', type=bool, default=False) # , help="Clean source after operation"
def compact(sources, dest, clean):
    _process(COMPACT, sources, dest, clean)

    if (clean):
        _rm_sources(sources)


@uaf_cli.command(name=EXTRACT)
@click.argument('sources', nargs=-1, type=click.Path(exists=True), required=True) # , help='List of elements to extract'
@click.option('--dest', nargs=1, type=click.Path(exists=False)) # , help="Path where store the output"
@click.option('--clean', type=bool, default=False) # , help="Clean source after operation"
def extract(sources, dest, clean):
    for source in sources:
        _process(EXTRACT, [source], dest, clean)
    
    if (clean):
        _rm_sources(sources)


@click.command(cls=click.CommandCollection, sources=[uaf_cli])
def cli():
    pass


if __name__ == '__main__':
    cli()
