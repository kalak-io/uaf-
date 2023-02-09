#!/usr/bin/env python
# coding: utf-8

from os import getcwd
from pathlib import Path

from click.testing import CliRunner

from uafm import cli, COMPACT, EXTRACT,DEFAULT_ARCHIVE_NAME

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
        result = runner.invoke(cli, [COMPACT, created_file, '--dest', f'/unknown/path/{DEFAULT_ARCHIVE_NAME}'])
        assert result.exit_code == 1
        assert isinstance(result.exception, TypeError)


  def test_default_compact(self, tmp_path, files):
      runner = CliRunner()
      with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(cli, [COMPACT, *list((map(str, files)))])
        assert result.exit_code == 0
        path = Path(f"{getcwd()}/{DEFAULT_ARCHIVE_NAME}")
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

