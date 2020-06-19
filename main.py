from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.routing import Mount

routes = [Mount('/static', StaticFiles(directory='static'), name='static')]

app = FastAPI(routes=routes)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def calculator(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})
