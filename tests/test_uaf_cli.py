#!/usr/bin/env python
# coding: utf-8

from os import getcwd, listdir, remove
from pathlib import Path

import pytest
from click.testing import CliRunner

from uaf_cli import cli
from constants import COMPACT, EXTRACT, DEFAULT_ARCHIVE

class TestCompactCommand:
  def test_compact_without_sources(self, tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
      result = runner.invoke(cli, [COMPACT])
      assert result.exit_code == 2
      assert "Error: Missing argument 'SOURCES...'." in result.output

  def test_compact_with_unknown_file(self, tmp_path):
      runner = CliRunner()
      with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(cli, [COMPACT, "file.txt"])
        assert result.exit_code == 2
        assert "Path 'file.txt' does not exist." in result.output

  def test_compact_with_wrong_dest(self, tmp_path, make_file):
      runner = CliRunner()
      with runner.isolated_filesystem(temp_dir=tmp_path):
        created_file = make_file()
        result = runner.invoke(cli, [COMPACT, created_file, '--dest', f'/unknown/path/{DEFAULT_ARCHIVE}'])
        assert result.exit_code == 1
        assert isinstance(result.exception, TypeError)


  def test_default_compact(self, tmp_path, files):
      runner = CliRunner()
      with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(cli, [COMPACT, *list((map(str, files)))])
        assert result.exit_code == 0
        path = Path(f"{getcwd()}/{DEFAULT_ARCHIVE}")
        assert path.exists()


  def test_compact_with_different_archive(self, tmp_path, files, archive):
      runner = CliRunner()
      with runner.isolated_filesystem(temp_dir=tmp_path):
          dest = Path(tmp_path / archive)
          result = runner.invoke(cli, [COMPACT, *list((map(str, files))), '--dest', Path(tmp_path / archive)])
          assert result.exit_code == 0
          assert dest.exists()


class TestExtractCommand:
  def test_extract_without_sources(self):
    runner = CliRunner()
    result = runner.invoke(cli, [EXTRACT])
    assert result.exit_code == 2
    assert "Error: Missing argument 'SOURCES...'." in result.output

  def test_extract_with_unknown_archive(self):
    runner = CliRunner()
    result = runner.invoke(cli, [EXTRACT, "archive.tar"])
    assert result.exit_code == 2
    assert "Path 'archive.tar' does not exist." in result.output

  def test_compact_with_wrong_dest(self, create_archive):
    with pytest.raises(Exception) as e:
      runner = CliRunner()
      with runner.isolated_filesystem():
        created_archive = create_archive()
        path = '/unknown/path/'
        result = runner.invoke(cli, [EXTRACT, created_archive, '--dest', path])
        count = listdir(path)
        assert result.exit_code == 1
        assert count == 1
    assert "[Errno 2] No such file or directory: '/unknown/path/'" in str(e.value) # this message
    assert e.type == FileNotFoundError

  def test_default_extract(self, tmp_path, files, create_archive):
    runner = CliRunner()
    with runner.isolated_filesystem():
      ls = listdir(tmp_path)
      assert len(ls) == len(files)
      created_archive = create_archive()
      ls = listdir(tmp_path)
      assert len(ls) == len(files) + 1
      for file in files:
        remove(file)
      ls = listdir(tmp_path)
      assert len(ls) == 1
      result = runner.invoke(cli, [EXTRACT, created_archive])
      assert result.exit_code == 0
      ls = listdir('.')
      assert len(ls) == len(files)

  def test_default_extract_with_destination(self, tmp_path, files, create_archive):
    runner = CliRunner()
    with runner.isolated_filesystem():
      ls = listdir(tmp_path)
      print("beginning")
      print(ls)
      assert len(ls) == len(files)
      created_archive = create_archive()
      ls = listdir(tmp_path)
      print("creating archive")
      print(ls)
      assert len(ls) == len(files) + 1
      for file in files:
        remove(file)
      ls = listdir(tmp_path)
      print("after removing")
      print(ls)
      assert len(ls) == 1
      print("created_archive")
      print(created_archive)
      print("tmp_path")
      print(tmp_path)
      result = runner.invoke(cli, [EXTRACT, created_archive, '--dest', tmp_path])
      assert result.exit_code == 0
      ls = listdir(tmp_path)
      print("after extracting")
      print(ls)
      assert len(ls) == len(files) + 1