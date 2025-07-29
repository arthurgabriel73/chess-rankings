from starlette.responses import JSONResponse

from src.main.infra.config.exception.failed_dependency_exception import FailedDependencyException
from src.main.main import app


@app.exception_handler(ValueError)
async def value_error_exception_handler(request, exc):
    return JSONResponse(status_code=400, content={'detail': str(exc)})


@app.exception_handler(FailedDependencyException)
async def failed_dependency_exception_handler(request, exc):
    return JSONResponse(status_code=424, content={'detail': str(exc.message)})
