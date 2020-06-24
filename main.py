from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.routing import Mount
from dbsetup import expressions
from requests import ExpressionRequest
from calculator import calculate

routes = [Mount('/static', StaticFiles(directory='static'), name='static')]

app = FastAPI(routes=routes)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def calculator(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})


@app.get("/history")
def history(request: Request):
    history = expressions.find({})

    return templates.TemplateResponse("history.html", {
        "request": request,
        "history": history
    })


@app.post("/")
def add_expression(expression_request: ExpressionRequest):

    res = calculate(expression_request.expression)

    new_expression = {
        "expression": expression_request.expression,
        "result": res
    }

    expressions.insert_one(new_expression)

    return {
        "status": "200",
        "message": "Expression added to db",
        "result": str(res)
    }


@app.delete("/history")
def delete_history():
    expressions.delete_many({})
    return {"status": "200", "message": "History cleared"}
