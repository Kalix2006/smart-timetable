from genetictabler import GenerateTimeTable

def generate_timetables(total_classes, no_courses, slots, total_days, daily_repetition):
    """
    Generate timetable options using genetic algorithm.

    Parameters:
    - total_classes: int, total classes to schedule
    - no_courses: int, number of distinct courses/subjects
    - slots: int, number of slots per day
    - total_days: int, number of days in timetable
    - daily_repetition: int, max repetition of courses per day

    Returns:
    - List of timetable solutions (dictionaries or strings describing the timetable)
    """
    table = GenerateTimeTable(total_classes, no_courses, slots, total_days, daily_repetition)
    results = []
    for timetable in table.run():
        results.append(timetable)
    return results


if __name__ == "__main__":
    # Example usage
    total_classes = 20
    no_courses = 5
    slots = 4
    total_days = 5
    daily_repetition = 1

    timetables = generate_timetables(total_classes, no_courses, slots, total_days, daily_repetition)
    for idx, tt in enumerate(timetables, start=1):
        print(f"Timetable Option {idx}:")
        print(tt)
