from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Simplified timetable generator
def generate_timetable(data):
    classrooms = data.get("classrooms", ["Room101", "Room102"])
    subjects = data.get("subjects", ["Math", "Physics", "Chemistry", "CS"])
    faculty = data.get("faculty", {
        "Math": ["Dr. A"],
        "Physics": ["Dr. B"],
        "Chemistry": ["Dr. C"],
        "CS": ["Dr. D"]
    })
    batches = data.get("batches", ["BatchA", "BatchB"])
    max_classes_per_day = data.get("max_classes_per_day", 3)
    faculty_leave = data.get("faculty_leave", {})  # e.g. {"Dr. B": ["Wednesday"]}

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    options = []

    for _ in range(3):  # Generate 3 different timetable options
        timetable = {}
        for batch in batches:
            timetable[batch] = []
            for day_index, day_name in enumerate(days):
                daily_classes = []
                subjects_day = random.sample(subjects, min(max_classes_per_day, len(subjects)))
                for sub in subjects_day:
                    possible_faculty = [f for f in faculty[sub]
                                        if day_name not in faculty_leave.get(f, [])]
                    if not possible_faculty:
                        faculty_sub = "No available faculty"
                    else:
                        faculty_sub = random.choice(possible_faculty)
                    classroom_sub = random.choice(classrooms)
                    daily_classes.append({
                        "subject": sub,
                        "faculty": faculty_sub,
                        "classroom": classroom_sub,
                        "day": day_name
                    })
                timetable[batch].append(daily_classes)
        options.append(timetable)
    return options

@app.route("/")
def home():
    return "Smart Timetable Scheduler Backend running!"

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()
    timetable_options = generate_timetable(data)
    return jsonify({"options": timetable_options})

if __name__ == "__main__":
    app.run(debug=True)
