import sys
import os
sys.path.append(
                os.path.abspath(
                    os.path.join(
                    os.path.dirname(__file__),
                '..')))

from fastapi import FastAPI
from app.routes import router

app = FastAPI()

#include routes
app.include_router(router)

#welcome route
@app.get("/")
def welcome():
    return {"message":"Welcome to the SVM Text Classification API"}

#uvicorn app.main:app --reload
#http://127.0.0.1:8000
#http://127.0.0.1:8000/docs (in browser)

