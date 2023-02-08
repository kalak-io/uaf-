import pytest
from pathlib import Path

from constants import CONFIG_MIME_TYPE


DEFAULT_FILENAME = "file.txt"
DEFAULT_ARCHIVE_NAME = "archive"
DEFAULT_CONTENT = "content"

AVAILABLE_EXTENSIONS = [suffix for suffixes in map(lambda value: value["suffix"], CONFIG_MIME_TYPE.values()) for suffix in suffixes]

@pytest.fixture
def make_file(tmp_path):
    def make(
        name: str = DEFAULT_FILENAME,
        content: str = DEFAULT_CONTENT,
        **rest
    ):
        file = tmp_path / Path(name)
        file.write_text(content)
        return file

    return make


@pytest.fixture(params=[1, 5])
def files(make_file, request):
    files = []
    for i in range(request.param):
        file = make_file(name=f'{i}_{DEFAULT_FILENAME}')
        files.append(file)
    return files


@pytest.fixture(params=AVAILABLE_EXTENSIONS)
def archive(tmp_path, request):
    return tmp_path / Path(f"{DEFAULT_ARCHIVE_NAME}{request.param}")
