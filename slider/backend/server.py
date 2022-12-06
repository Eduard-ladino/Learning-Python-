from fastapi import FastAPI
import json

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/slider")
def read_root():
    data = None
    with open("data.json") as f:
        data = json.load(f)
    return data
