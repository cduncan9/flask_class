# server.py
# jsonify will turn almost anything into a
# string that can be sent over the internet
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_on():
    return "The server is on."


@app.route("/info", methods=["GET"])
def info():
    info_string = "This server calculates the ideal"
    " weight of a person based off of their height, "
    "age and gender."
    calc_info_string = "This calculation can accept a POST"
    out_dictionary = {"info": info_string, "calc_info": calc_info_string}
    return jsonify(out_dictionary)


@app.route("/iwc", methods=["POST"])
def ideal_weight():
    in_data = request.get_json()
    age = in_data["age"]
    gender = in_data["gender"]
    height = in_data["height_in"]

    ideal_weight_kg = 48.0 + 2.7 * (height - 60)
    ideal_weight_lb = ideal_weight_kg * 2.20462

    answer = {"input_data": in_data, "ideal_weight": ideal_weight_lb}
    return jsonify(answer)


@app.route("/hello/<yourname>", methods=["GET"])
def say_hello(yourname):
    return "Hello, {}".format(yourname)


if __name__ == '__main__':
    app.run()
