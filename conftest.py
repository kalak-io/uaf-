#!/usr/bin/env python
# coding: utf-8
from shutil import make_archive

import pytest
from pathlib import Path
from os import path

from constants import DEFAULT_FILENAME, DEFAULT_CONTENT, AVAILABLE_EXTENSIONS, DEFAULT_ARCHIVE_NAME, DEFAULT_ARCHIVE_EXTENSION


@pytest.fixture
def make_file(tmp_path):
    def make(
        filename: str = DEFAULT_FILENAME,
        content: str = DEFAULT_CONTENT,
        **rest
    ):
        file = tmp_path / Path(filename)
        file.write_text(content)
        return file

    return make


@pytest.fixture(params=[1, 5])
def files(make_file, request):
    files = []
    for i in range(request.param):
        file = make_file(filename=f'{i}_{DEFAULT_FILENAME}')
        files.append(file)
    return files


@pytest.fixture(params=AVAILABLE_EXTENSIONS)
def archive(tmp_path, request):
    return tmp_path / Path(f"{DEFAULT_ARCHIVE_NAME}{request.param}")


@pytest.fixture
def create_archive(tmp_path, files):
    def make(
        filename: str = DEFAULT_ARCHIVE_NAME,
        extension: str = DEFAULT_ARCHIVE_EXTENSION,
        **rest
    ):
        archive = make_archive(tmp_path / Path(filenqame), extension[1:], tmp_path)
        return archive
    return make