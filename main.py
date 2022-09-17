from fastapi import FastAPI
from cohere_stuff import get_idea

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Hello World"}
    
@app.get("/generate")
def generate_post():
  return get_idea()
