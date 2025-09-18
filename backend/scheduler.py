import random

def allocate_room(subject_size, classrooms, allocated_rooms):
    for room in classrooms:
        if room["capacity"] >= subject_size and room["name"] not in allocated_rooms:
            allocated_rooms.add(room["name"])
            return room["name"]
    return "No suitable room"

def generate_timetable(data):
    classrooms = data.get("classrooms", [{"name": "Room101", "capacity": 50}, {"name": "Lab1", "capacity": 30}])
    subjects = data.get("subjects", ["Math", "Physics", "Chemistry", "CS"])
    faculty = data.get("faculty", {
        "Math": ["Dr. A"],
        "Physics": ["Dr. B"],
        "Chemistry": ["Dr. C"],
        "CS": ["Dr. D"]
    })
    subject_sizes = data.get("subject_sizes", {"Math":40, "Physics":25, "Chemistry":30, "CS":35})
    batches = data.get("batches", ["BatchA", "BatchB"])
    max_classes_per_day = data.get("max_classes_per_day", 3)
    faculty_leave = data.get("faculty_leave", {})
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    options = []

    for _ in range(3):
        timetable = {}
        for batch in batches:
            timetable[batch] = []
            daily_allocated_rooms = {day: set() for day in days}
            for day_name in days:
                daily_classes = []
                subjects_day = random.sample(subjects, min(max_classes_per_day, len(subjects)))
                for sub in subjects_day:
                    possible_faculty = [f for f in faculty[sub] if day_name not in faculty_leave.get(f, [])]
                    if not possible_faculty:
                        faculty_sub = "No available faculty"
                    else:
                        faculty_sub = random.choice(possible_faculty)
                    room = allocate_room(subject_sizes.get(sub, 30), classrooms, daily_allocated_rooms[day_name])
                    daily_classes.append({
                        "subject": sub,
                        "faculty": faculty_sub,
                        "classroom": room,
                        "day": day_name
                    })
                timetable[batch].append(daily_classes)
        options.append(timetable)
    return options
