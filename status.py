from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import info

app = FastAPI()
system_info = info.Info()
# read use utf-8
index_html = open("index.html", "r", encoding="utf-8").read()


@app.get("/status")
async def read_system_status():
    status = await system_info.get_system_status()
    return status


@app.get("/", response_class=HTMLResponse)
async def index():
    return index_html
