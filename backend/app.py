from flask import Flask, request, jsonify
from flask_cors import CORS
import random

from scheduler import generate_timetable
from genetic_scheduler import generate_timetables as generate_genetic_timetables

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Smart Timetable Scheduler Backend running!"

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()
    timetable_options = generate_timetable(data)
    return jsonify({"options": timetable_options})

approved_timetables = []

@app.route("/api/approve", methods=["POST"])
def approve():
    data = request.get_json()
    approved_option = data.get("approved_option")
    timetable = data.get("timetable")
    approved_timetables.append({"option": approved_option, "timetable": timetable})
    return jsonify({"message": f"Timetable option {approved_option} approved and saved."})

@app.route("/api/generate/genetic", methods=["POST"])
def generate_genetic():
    # For testing, return one timetable variant same as regular scheduler format
    data = request.get_json()
    timetable_options = generate_timetable(data)  # reuse regular generator temporarily
    return jsonify({"options": [timetable_options[0]]})


if __name__ == "__main__":
    app.run(debug=True)
