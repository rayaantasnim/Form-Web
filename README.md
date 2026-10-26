<div align="center">

# 🎓 Student Registration Portal

A fast, responsive, and lightweight web application built with **FastAPI**, **Jinja2 Templates**, and **HTML5/CSS3** to streamline student registration workflows.

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)](https://jinja.palletsprojects.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

</div>

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Tech Stack Overview](#-tech-stack-overview)
- [Project Architecture](#-project-architecture)
- [Directory Structure](#-directory-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Documentation](#-api-documentation)
- [UI Walkthrough & Previews](#-ui-walkthrough--previews)
- [Expandable Deep-Dives](#-expandable-deep-dives)
- [License](#-license)
- [Author & Footer](#-author--footer)

---

## 🚀 Overview

The **Student Registration Portal** is a full-stack, server-side rendered application designed for quick user onboarding and data dynamic visualization. Utilizing FastAPI's asynchronous handling and Jinja2 templating engine, the system captures student details—including name, age, email, and phone number—and renders a formatted dynamic receipt card upon submission.

---

## ✨ Key Features

- ⚡ **High Performance Backend**: Powered by FastAPI and Starlette.
- 🎨 **Responsive UI/UX**: Custom, modern CSS styling with flexbox layout and smooth visual focus states.
- 🛡️ **Form Data Validation**: Automatic server-side parsing and field handling using FastAPI `Form(...)` objects.
- 📁 **Static Asset Management**: Integrated FastAPI static directory mounting for optimized stylesheet delivery.
- 📄 **Dynamic Templating**: Dynamic HTML rendering via Jinja2 engine.

---

## 🛠️ Tech Stack Overview

| Layer | Technology | Description |
| :--- | :--- | :--- |
| **Backend Framework** | [FastAPI](https://fastapi.tiangolo.com/) | Modern, fast (high-performance) web framework for Python. |
| **Template Engine** | [Jinja2](https://jinja.palletsprojects.com/) | Expressive and extensible Python templating language. |
| **Styling** | [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) | Custom modular styling (`style.css` and `result.css`). |
| **Markup** | [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML) | Clean, semantic web structure. |
| **Server** | [Uvicorn](https://www.uvicorn.org/) | Lightning-fast ASGI server implementation. |

---

## 🏗️ Project Architecture

```
                                +-----------------------+
                                |      Web Browser      |
                                +-----------+-----------+
                                            |
                                 1. GET /   |   2. Render Form Page
                                            v
                                +-----------------------+
                                |  FastAPI App Engine   |
                                +-----------+-----------+
                                            |
                                 3. POST /register      |   4. Dynamic Template Processing
                                 (Form Data Payload)    v
                                +-----------------------+
                                |   Jinja2 Templates    |
                                |  (index.html / result)|
                                +-----------------------+
```

---

## 📂 Directory Structure

```text
├── main.py                  # Core FastAPI application entry point
├── static/
│   └── css/
│       ├── style.css        # Stylesheet for registration form
│       └── result.css       # Stylesheet for summary receipt page
└── templates/
    ├── index.html           # Main registration form page
    └── result.html          # Confirmation and summary page
```

---

## 🏁 Getting Started

### Prerequisites

Ensure you have **Python 3.8+** installed on your system.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/student-registration-portal.git
   cd student-registration-portal
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn jinja2 python-multipart
   ```

### Running the Application

Launch the Uvicorn development server:

```bash
uvicorn main:app --reload
```

Open your browser and navigate to `http://127.0.0.1:8000` to view the application.

---

## 📑 API Documentation

Once the server is running, you can access interactive API documentation provided by FastAPI:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Endpoints Summary

| Method | Endpoint | Description | Query/Body Params | Response |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/` | Serves the registration form page | None | `HTMLResponse` (`index.html`) |
| `POST` | `/register` | Processes submission and displays results | `name`, `age`, `email`, `mobile` | `HTMLResponse` (`result.html`) |

---

## 🖼️ UI Walkthrough & Previews

<div align="center">

### System Interface Preview

| Registration Form (`index.html`) | Registration Summary (`result.html`) |
| :---: | :---: |
| <img src="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&w=500&q=80" width="350" alt="Form Interface"/> | <img src="https://images.unsplash.com/photo-1517842645767-c639042777db?auto=format&fit=crop&w=500&q=80" width="350" alt="Summary Interface"/> |

</div>

---

## 🔍 Expandable Deep-Dives

<details>
<summary><b>📂 View Backend Logic (<code>main.py</code>)</b></summary>

<br>

```python
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
```
</details>

<details>
<summary><b>🎨 View CSS Architecture (<code>style.css</code> & <code>result.css</code>)</b></summary>

<br>

#### **Registration Style (`style.css`)**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    margin: 0;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.container {
    background: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    max-width: 400px;
    width: 100%;
}

h1 {
    color: #333;
    font-size: 24px;
    margin-bottom: 20px;
    text-align: center;
}

h2 {
    color: #555;
    font-size: 18px;
}

label {
    display: block;
    margin-bottom: 5px;
    color: #666;
    font-weight: bold;
}

input {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

button {
    width: 100%;
    padding: 12px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.info-box {
    background: #e9ecef;
    padding: 15px;
    border-radius: 4px;
    margin-top: 15px;
}

.info-box p {
    margin: 8px 0;
    color: #333;
}
```

#### **Result Summary Style (`result.css`)**
```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f4f7f6;
    color: #333333;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

center, .container {
    background-color: #ffffff;
    padding: 2.5rem;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    max-width: 450px;
    width: 100%;
    box-sizing: border-box;
    text-align: center;
}

h1 {
    color: #2c3e50;
    font-size: 1.8rem;
    margin-bottom: 0.5rem;
}

h2 {
    color: #16a085;
    font-size: 1.3rem;
    font-weight: 600;
    margin-top: 0;
    margin-bottom: 2rem;
    border-bottom: 2px solid #eef2f5;
    padding-bottom: 0.75rem;
}

p {
    font-size: 1rem;
    background-color: #f8fafc;
    margin: 0.75rem 0;
    padding: 0.85rem 1rem;
    border-radius: 6px;
    border-left: 4px solid #16a085;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 500;
}

p strong, p span {
    color: #555555;
    font-weight: 400;
}
```
</details>

---

## 📜 License

This project is open-source software licensed under the [MIT License](LICENSE).

---

<div align="center">

Authorized by Rayaan Tasnim 
&copy; All rights reserved

</div>