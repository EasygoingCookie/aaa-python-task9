from what_is_year_now import what_is_year_now
import pytest
from unittest.mock import patch
import io


def test_can_read_dmy_with_dots():
    """Can what_is_year_now read dmy-format?"""
    test = io.StringIO('{"currentDateTime": "20.02.1992"}')
    expected = 1992
    with patch('what_is_year_now.urllib.request.urlopen', return_value=test):
        input = what_is_year_now()
        assert input == expected, (
            'what_is_year_now() cant read dmy-format'
        )


def test_can_read_ymd_with_dashes():
    """Can what_is_year_now read dmy-format?"""
    test = io.StringIO('{"currentDateTime": "1993-02-20"}')
    expected = 1993
    with patch('what_is_year_now.urllib.request.urlopen', return_value=test):
        input = what_is_year_now()
        assert input == expected, (
            'what_is_year_now() cant read ymd-format'
        )


def test_cant_open_wrong_file():
    """Can what_is_year_now detect wrong type?"""
    wrong = '{"currentDateTime": "1993.20.02"}'
    with patch('what_is_year_now.urllib.request.urlopen', return_value=wrong):
        with pytest.raises(AttributeError):
            what_is_year_now()


def test_can_detect_wrong_format():
    """Can what_is_year_now detect wrong format?"""
    wrong2 = io.StringIO('{"currentDateTime": "1993.20.02"}')
    with patch('what_is_year_now.urllib.request.urlopen', return_value=wrong2):
        with pytest.raises(ValueError):
            what_is_year_now()
