from behave import *


@given('I put <thing> in a blender,')
def step_impl(context):
    assert context.failed is False

@when('I switch the blender on')
def step_impl(context):
    assert True is not False

@then('it should transform into <other thing>')
def step_impl(context):
    assert context.failed is False

