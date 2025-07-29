from behave import given, then, when


@given('I have a request to view the top "{num_players}" players for the "{category}" category')
def step_impl(context, num_players: int, category: str):
    context.request_url = f'/players/top/{category}/{num_players}'
    context.headers = {'Content-Type': 'application/json'}


@when('I send the request to view top players')
def step_impl(context):
    context.response = context.client.get(context.request_url, headers=context.headers)


@then('the response should contain a list of top players usernames for that category')
def step_impl(context):
    response_data = context.response.json()
    assert isinstance(response_data, dict)
    assert len(response_data['usernames']) == 50
