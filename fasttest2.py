from typing import Union
from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/')
async def root():
     return {"message": "Hello World."}
