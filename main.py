#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify
from cohere_stuff import get_idea
from flask_cors import CORS
from flask_cors import cross_origin
app = Flask(__name__)
CORS(app)


@cross_origin
@app.get("/")
def read_root():
    return jsonify({"message": "Hello World"})


@cross_origin
@app.get("/generate")
def generate_post():
    return jsonify(get_idea())


@cross_origin
@app.get("/generate/<category>")
def generate_post_with_category(category):
    print('The category is: ' + category)
    return jsonify(get_idea(category))


def main():
    app.run()


if __name__ == "__main__":
    main()
