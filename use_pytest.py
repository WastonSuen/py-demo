# #===========xx=====================####===================xx==============# #
# use pytest fixture
# #===========xx=====================####===================xx==============# #
import pytest


@pytest.fixture(params=['1', '2'])
def before(request):
    print "****** before: %s ******" % request.param
    yield request.param


def test1(before):
    print "test1: %s" % before


@pytest.mark.usefixtures("before")
def test2():
    print "test2"


# #===========xx=====================####===================xx==============# #
# use pytest fixture with params
# #===========xx=====================####===================xx==============# #

# method 1
@pytest.fixture(params=[{'status': 200}, {'status': 201}])
def fixture_need_to_be_tested(request):
    yield request.param
    # Could be called when testcase clean up
    print "****** after called:%s ******" % request.param


def test_need_to_be_tested(fixture_need_to_be_tested):
    resp = fixture_need_to_be_tested
    print resp


# method 2
def add(a, b):
    return a + b


@pytest.mark.parametrize("test_input, expected", [
    ([1, 1], 2),
    ([2, 2], 4),
    ([0, 1], 1),
])
def test_add(test_input, expected):
    assert expected == add(test_input[0], test_input[1])


# #===========xx=====================####===================xx==============# #
# use pytest fixture and mock at the same time
# #===========xx=====================####===================xx==============# #

import pytest
import os.path
from mock import patch


def exists(path):
    return os.path.exists(path)


@patch('os.path.exists')
@pytest.mark.parametrize('path, expect', [('/foo', True), ('/bar', False)])
def test_exists(mock_exists, path, expect):
    def side_effect(args):
        return expect

    mock_exists.side_effect = side_effect
    assert exists(path) == expect


class Check(object):
    def exists(self, path):
        return os.path.exists(path)


@patch.object(Check, 'exists')
@pytest.mark.parametrize('path, expect', [('/foo', True), ('/bar', False)])
def test_exists2(mock_exists, path, expect):
    def side_effect(args):
        return expect

    mock_exists.side_effect = side_effect
    check = Check()
    assert check.exists(path) == expect
