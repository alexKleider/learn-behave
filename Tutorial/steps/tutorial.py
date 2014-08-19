#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# Copyright 2014 Alex Kleider; All Rights Reserved.

# file: 'tutorial.py'
""" A 'behave' executable taken from the Tutorial- 1st example."""
print('Running tutorial.py: ')
print('"""')
print(__doc__)
print('"""')

from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
