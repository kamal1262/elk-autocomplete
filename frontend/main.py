import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates



app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index():
    return { "message": "hello world"}

@app.get("/items/{id}", response_class = HTMLResponse)
async def ream_item(request: Request, id: str):

    return templates.TemplateResponse("home.html", {"request":request, "id": id })

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)


# import os
# ​
# from fastapi import FastAPI
# from mangum import Mangum
# import uvicorn
# ​
# stage = os.environ.get('STAGE', None)
# openapi_prefix = f"/{stage}" if stage else "/"
# ​
# app = FastAPI(title="MyAwesomeApp", openapi_prefix=openapi_prefix) # Here is the magic
# ​
# ​
# @app.get("/hello")
# def hello_world():
#     return {"message": "Hello World"}
# ​
# ​
# handler = Mangum(app)