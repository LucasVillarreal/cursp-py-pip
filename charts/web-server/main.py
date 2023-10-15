import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4]

@app.get('/contact/', response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>Contact</title>
        </head>
        <body>
            <h1>Lucas Villarreal</h1>
            <p>3498 441990</p>
        </body>
    </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()
