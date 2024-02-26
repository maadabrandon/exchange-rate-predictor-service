from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from config import settings

from src.logger import get_console_logger
from src.model_serving.api import api_router


logger = get_console_logger()

frontend_app = FastAPI(
  title=settings.comet_project_name,
  openapi_url=settings.API_V1_STR
)

root_router = APIRouter()

@root_router
def index(request:Request) -> Any:
  
  body = (
    "<html>"
    "<body style='padding: 10px;'>"
    "<h1>Welcome to the Model API</h1>"
    "<div>"
    "Check the docs: <a href='/docs'>here</a>"
    "</div>"
    "</body>"
    "</html>"
  )
  
  return HTMLResponse(content=body)


frontend_app.include_router(
  router=api_router, prefix=settings.API_V1_STR
)

frontend_app.include_router(router=root_router)


if __name__ == "__main__":
  
  logger.warning("Running in development mode.")
  
  import uvicorn
  
  uvicorn.run(
    app = frontend_app,
    host="localhost",
    port=8001,
    log_level="debug"
  )