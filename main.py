from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount('/css', StaticFiles(directory='static/css'), name='css')
app.mount('/js', StaticFiles(directory='static/js'), name='js')

templates = Jinja2Templates(directory="templates")


@app.get('/')
async def fuck(request: Request):
    return templates.TemplateResponse("index.html", {'request':request})
