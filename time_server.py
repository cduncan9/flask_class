from flask import Flask, jsonify, request
from datetime import datetime, time

app = Flask(__name__)


@app.route("/time", methods=["GET"])
def current_time():
    x = datetime.now()
    y = datetime.strftime(x, "%H:%M:%S")
    return jsonify(y)


@app.route("/date", methods=["GET"])
def current_date():
    x = datetime.now()
    y = datetime.strftime(x, "%m-%d-%y")
    return jsonify(y)


@app.route("/age", methods=["POST"])
def user_age():
    in_data = request.get_json()
    in_date = in_data["date"]
    in_time = in_date.split("/")
    in_days, in_months, in_years = in_time[1], in_time[0], in_time[2]
    in_datetime = datetime(int(in_years), int(in_months), int(in_days))
    units = in_data["units"]
    date_now = datetime.now()
    diff = date_now - in_datetime
    return jsonify(diff.days)


@app.route("/until_next_meal/<meal>", methods=["GET"])
def until_meal(meal):
    time_now = datetime.now().time()
    meal_times = {'breakfast': time(8, 30, 0), 'lunch': time(12, 30, 0),
                  'dinner': time(19, 30, 0)}
    time_until_hours = meal_times[meal].hour - time_now.hour
    if time_until_hours < 0:
        time_until_hours += 24
    time_until_minutes = meal_times[meal].minute - time_now.minute
    if time_until_minutes < 0:
        time_until_minutes += 60
    time_until_seconds = meal_times[meal].second - time_now.second
    if time_until_seconds < 0:
        time_until_seconds += 60
    time_string = "{} is in {} hours, {} minutes, and {} seconds.".format(meal,
                                                                          time_until_hours,
                                                                          time_until_minutes,
                                                                          time_until_seconds)
    return jsonify(time_string)


if __name__ == "__main__":
    app.run()