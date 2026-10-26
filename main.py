from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html"
        )

@app.post("/register")
def register(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    email: str = Form(...),
    mobile: str = Form(...)
):
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        
        context = {
            "request": request, 
            "name": name, 
            "age": age, 
            "email": email, 
            "mobile": mobile
        }
    )
