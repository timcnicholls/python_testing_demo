#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_testing_demo` package."""

import pytest


from python_testing_demo import python_testing_demo


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

def test_add():

    first = 1
    second = 2
    sum = first + second

    assert python_testing_demo.add(first, second) == sum


def test_subtract():

    first = 1
    second = 2
    difference = first - second
    
    assert python_testing_demo.subtract(first, second) == difference