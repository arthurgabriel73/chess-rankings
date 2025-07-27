import starlette.responses as _responses
import uvicorn
from fastapi import FastAPI

from src.main.infra.config.environment_settings import get_environment_variables

app = FastAPI(title='Chess Rankings API', description='An API to fetch and manage chess players rankings.')


@app.get('/')
async def read_root():
    return _responses.RedirectResponse('/docs')


if __name__ == '__main__':
    env = get_environment_variables()
    uvicorn.run('main:app', host=env.APP_HOST, port=env.APP_PORT, log_level='info', reload=True)
