from datetime import datetime, timedelta
from typing import Any

import pandas as pd
from behave import given, then, when


@given(
    'I have a request to generate a CSV file for the rating histories of the top "{num_players}" players for the "{category}" category for the previous "{num_days}" days'
)
def step_impl(context, num_players: str, category: str, num_days: str):
    context.request_url = f'/players/top/rating-history/{category}/{num_players}/generate-file?num_days={num_days}'
    context.headers = {'Content-Type': 'application/json'}


@when('I send the request to generate the CSV file')
def step_impl(context):
    context.response = context.client.post(context.request_url, headers=context.headers)


@then(
    'the response should contain a CSV file with the rating histories of the top "{num_players}" players for the "{category}" category for the previous "{num_days}" days'
)
def step_impl(context, num_players: str, category: str, num_days: str):
    response_data = context.response.json()
    assert isinstance(response_data, dict), 'Response data should be a dictionary'
    assert 'success' in response_data, "Response does not contain 'success' field"
    assert response_data['success'] is True, "Response 'success' field should be True"
    assert 'file_url' in response_data, "Response does not contain 'file_url' field"
    assert 'download_url' in response_data, "Response does not contain 'download_url' field"
    processed_data: Any = pd.read_csv(response_data['file_url'], sep=',', header=0, encoding='utf-8')
    data = processed_data.to_dict(orient='records')
    assert is_csv_data_correct(data, num_players, num_days), 'CSV file does not contain valid data'


def is_csv_data_correct(data: Any, num_players: str, num_days: str) -> bool:
    thirty_days_ago = datetime.now() - timedelta(days=30)
    for i in range(int(num_players)):
        if data[i]['username'] != f'User{i + 1}':
            return False
        for j in range(int(num_days) + 1):
            expected_date = (thirty_days_ago + timedelta(days=j)).strftime('%Y-%m-%d')
            if data[i][expected_date] is None:
                return False
    return True
