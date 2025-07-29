from starlette import status

error_responses = {
    status.HTTP_400_BAD_REQUEST: {
        'description': 'Invalid request parameters',
        'content': {
            'application/json': {
                'example': {'detail': 'Invalid category: must be one of: bullet, blitz, rapid, classical, ultraBullet'}
            }
        },
    },
    status.HTTP_424_FAILED_DEPENDENCY: {
        'description': 'Failed to fetch data from external service',
        'content': {'application/json': {'example': {'detail': 'Failed to fetch data from external service'}}},
    },
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        'description': 'Unprocessable entity',
        'content': {
            'application/json': {'example': {'detail': 'Invalid value for num_players: must be a positive integer'}}
        },
    },
}
