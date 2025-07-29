from behave import given, then, when


@given('I have a valid request to view top players for a specific category')
def step_impl(context):
    context.request_url = '/players/top/classical/50'
    context.headers = {'Content-Type': 'application/json'}


@when('I send the request to view top players')
def step_impl(context):
    context.response = context.client.get(context.request_url, headers=context.headers)


@then('the response should contain a list of top players usernames for that category')
def step_impl(context):
    response_data = context.response.json()
    assert isinstance(response_data, dict)
    assert len(response_data['usernames']) == 50
