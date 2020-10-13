def get_list_from_input(count):
    return [input() for _ in range(count)]


def get_students_marks_count(collection):
    student_marks = {}

    for value in collection:
        student, mark = value.split(' ')
        if student not in student_marks:
            student_marks[student] = []
        student_marks[student].append(float(mark))

    return student_marks


def get_average(collection):
    return sum(collection) / len(collection)


def print_results(student_marks):
    for student, marks in student_marks.items():
        average = get_average(marks)
        marks_string = ' '.join((f'{mark:.2f}' for mark in marks))
        print(f'{student} -> {marks_string} (avg: {average:.2f})')


print_results(get_students_marks_count(get_list_from_input(int(input()))))


