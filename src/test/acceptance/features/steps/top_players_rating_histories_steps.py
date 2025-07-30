from behave import given, then, when


@given(
    'I have a request to view the rating histories of the top "{num_players}" players for the "{category}" category for the previous "{num_days}" days'
)
def step_impl(context, num_players: int, category: str, num_days: int):
    context.request_url = f'/players/top/rating-history/{category}/{num_players}?num_days={num_days}'
    context.headers = {'Content-Type': 'application/json'}


@when('I send the request to view top players rating histories')
def step_impl(context):
    context.response = context.client.get(context.request_url, headers=context.headers)


@then(
    'the response should contain a list of top "{num_players}" players rating histories for the "{category}" category for the previous "{num_days}" days'
)
def step_impl(context, num_players: int, category: str, num_days: int):
    response_data = context.response.json()
    assert isinstance(response_data, dict), 'Response data should be a dictionary'
    assert len(response_data['histories']) == int(num_players)
    for record in response_data['histories']:
        assert 'player' in record
        assert 'history' in record
        assert isinstance(record['history'], dict)
        assert len(record['history']) == int(num_days) + 1
