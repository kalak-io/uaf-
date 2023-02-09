#!/usr/bin/env python
# coding: utf-8

import utils

class TestValidateFilepath:
    def test_wrong_filepath(self):
        result = utils.validate_filepath("/bab/path/archive.tar")
        assert result == False

    def test_right_filepath(self, tmp_path):
        result = utils.validate_filepath(f'{tmp_path}/archive.tar')
        assert result == True