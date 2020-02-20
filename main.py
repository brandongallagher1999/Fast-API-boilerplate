import sys
sys.path.append("./modules/api/")
sys.path.append("./modules/config/")
from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from config_manager import ConfigManager



# App instance and configurations -----------

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory = "./templates")

config = ConfigManager()


#--------------------------------------------

# Routes ------------------------------------

@app.get("/")
async def root(r: Request):
    '''
    Main page, base root endpoint.

    @returns: HTML -> HTML Template
    '''

    return templates.TemplateResponse("index.html", r)

#--------------------------------------------