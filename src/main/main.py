import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.main.infra.adapter.driver.rest.player_controller import players_router
from src.main.infra.config.environment_settings import get_environment_variables

app = FastAPI(title='Chess Rankings API', description='An API to fetch and manage chess players rankings.')
# FastAPI: a Python class that provides all the functionality for your API.
# app: an "instance" of the class FastAPI, the main point of interaction.

from src.main.infra.config.custom_exception_handler import *  # important: to load custom exception handlers


@app.get('/')
def read_root():
    return RedirectResponse('/docs')


# RedirectResponse: returns an HTTP redirect. Uses a 307 status code by default.


app.include_router(players_router)
# include_router: Includes an APIRouter in the same app.

if __name__ == '__main__':
    # this is like the entrypoint of the file execution
    # the variable __name__ represents the module name. However, when the module is run by itself as a program,
    # __name__ is defined to ’__main__’, different from when the module is imported, in which the value is in fact equal to the module name.

    env = get_environment_variables()
    uvicorn.run('main:app', host=env.APP_HOST, port=env.APP_PORT, log_level='info', reload=True)
