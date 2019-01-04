from PIL import Image
from flask import Flask
from flask import request
from flask import jsonify
import matlab.engine
import os
import random
import sys

app = Flask(__name__)
engine = matlab.engine.start_matlab()


@app.route("/")
def hello():
    return "Hello, the server is functioning."


@app.route("/detect", methods=["POST"])
def detect():
    name = request.form.get("name")
    type = request.form.get("type")
    file = Image.open(request.files["file"])
    file = file.convert("RGB")

    if name == "laura":
      file.save("../matlab/laura/DataUji/gambar.jpg")
    elif name == "vita":
      file.save("../matlab/vita/DataUji/gambar.jpg")
    elif name == "farisa":
      file.save("../matlab/farisa/DataUji/gambar.jpg")
    elif name == "fika":
      file.save("../matlab/fika/DataUji/gambar.jpg")

    result = process(name)

    response = {}
    response["hasil"] = result
    return jsonify(response)


def check_offline(name):
    engine1 = matlab.engine.start_matlab()
    result = engine1.main_matlab(name)
    print result


def process(name):
    return engine.main_matlab(name)


if __name__ == "__main__":
    print sys.argv[1]
    check_offline(sys.argv[1])
