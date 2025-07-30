from fastapi.testclient import TestClient

from src.main.infra.config.environment_settings import get_environment_variables
from src.main.main import app

env = get_environment_variables()


def before_all(context):
    context.client = TestClient(app)


def after_all(context):
    context.client.close()
