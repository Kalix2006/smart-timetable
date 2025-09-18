import random

def allocate_room(subject_size, classrooms):
    for room in classrooms:
        if room["capacity"] >= subject_size:
            return room["name"]
    return "No suitable room"

def generate_timetable(data):
    classrooms = data["classrooms"]  # List of dicts: [{name, capacity}, ...]
    subjects = data["subjects"]      # List of subject names
    faculty = data["faculty"]        # Dict: subject -> list of faculty
    batches = data["batches"]        # List of batch names
    max_classes_per_day = data["max_classes_per_day"]
    subject_sizes = data["subject_sizes"]  # Dict: subject -> required batch size
    faculty_leave = data.get("faculty_leave", {})  # Dict: faculty -> list of day names

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    options = []
    for _ in range(3):  # Generate 3 variants
        timetable = {}
        for batch in batches:
            timetable[batch] = []
            for day_index, day_name in enumerate(week_days):
                daily_classes = []
                subjects_day = random.sample(subjects, min(max_classes_per_day, len(subjects)))
                for sub in subjects_day:
                    # Faculty allocation considering leave
                    possible_faculty = [
                        f for f in faculty[sub]
                        if day_name not in faculty_leave.get(f, [])
                    ]
                    faculty_sub = random.choice(possible_faculty) if possible_faculty else "No available faculty"

                    # Room allocation based on class size
                    subject_size = subject_sizes[sub]
                    classroom_sub = allocate_room(subject_size, classrooms)

                    daily_classes.append({
                        "subject": sub,
                        "faculty": faculty_sub,
                        "classroom": classroom_sub,
                    })
                timetable[batch].append(daily_classes)
        options.append(timetable)
    return options
