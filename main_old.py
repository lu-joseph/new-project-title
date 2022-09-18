from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cohere_stuff import get_idea

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost"],
#     allow_credentials=False,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/generate")
def generate_post():
    return get_idea()
