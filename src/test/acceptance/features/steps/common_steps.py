from behave import then


@then('I should receive a response with status code 200')
def step_impl(context):
    assert context.response.status_code == 200, f'Expected status code 200, but got {context.response.status_code}'


@then('I should receive a response with status code 400')
def step_impl(context):
    assert context.response.status_code == 400, f'Expected status code 400, but got {context.response.status_code}'


@then('I should receive a response with status code 424')
def step_impl(context):
    assert context.response.status_code == 424, f'Expected status code 424, but got {context.response.status_code}'


@then('I should receive a response with status code 422')
def step_impl(context):
    assert context.response.status_code == 422, f'Expected status code 422, but got {context.response.status_code}'
