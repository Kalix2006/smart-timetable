from genetictabler import GenerateTimeTable

def generate_timetables(total_classes, no_courses, slots, total_days, daily_repetition):
    table = GenerateTimeTable(total_classes, no_courses, slots, total_days, daily_repetition)
    results = []
    for timetable in table.run():
        results.append(timetable)
    return results

if __name__ == "__main__":
    total_classes = 20
    no_courses = 5
    slots = 4
    total_days = 5
    daily_repetition = 1
    timetables = generate_timetables(total_classes, no_courses, slots, total_days, daily_repetition)
    for idx, tt in enumerate(timetables, start=1):
        print(f"Timetable Option {idx}:")
        print(tt)
