from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def main():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard</title>
    </head>
    <body>
        <h1>Welcome to the Dashboard</h1>
        <p>This is your dashboard page.</p>
        <p>Update Test</p>
    </body>
    </html>
    """
