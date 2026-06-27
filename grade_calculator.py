# Student Grade Calculator
# Author: Rajakhunnisa Shaik
# Description: A simple Python program to calculate student grades and GPA

def get_grade_letter(percentage):
    """Returns letter grade based on percentage."""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def get_grade_points(letter):
    """Returns grade points for GPA calculation."""
    grade_points = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return grade_points.get(letter, 0.0)

def calculate_weighted_average(subjects):
    """Calculates weighted average based on credits."""
    total_weighted = 0
    total_credits = 0
    for subject in subjects:
        total_weighted += subject['percentage'] * subject['credits']
        total_credits += subject['credits']
    if total_credits == 0:
        return 0
    return total_weighted / total_credits

def calculate_gpa(subjects):
    """Calculates GPA on a 4.0 scale."""
    total_points = 0
    total_credits = 0
    for subject in subjects:
        letter = get_grade_letter(subject['percentage'])
        points = get_grade_points(letter)
        total_points += points * subject['credits']
        total_credits += subject['credits']
    if total_credits == 0:
        return 0.0
    return round(total_points / total_credits, 2)

def get_pass_fail(percentage):
    """Returns Pass or Fail status."""
    return "Pass" if percentage >= 60 else "Fail"

def print_report(student_name, subjects):
    """Prints the full grade report."""
    print("\n" + "=" * 55)
    print(f"         STUDENT GRADE REPORT")
    print("=" * 55)
    print(f"Student Name : {student_name}")
    print("-" * 55)
    print(f"{'Subject':<20} {'Marks':>6} {'%':>6} {'Grade':>6} {'Status':>8}")
    print("-" * 55)

    for subject in subjects:
        pct = subject['percentage']
        letter = get_grade_letter(pct)
        status = get_pass_fail(pct)
        marks_display = f"{subject['marks_obtained']}/{subject['max_marks']}"
        print(f"{subject['name']:<20} {marks_display:>6} {pct:>5.1f}% {letter:>6} {status:>8}")

    print("-" * 55)
    weighted_avg = calculate_weighted_average(subjects)
    gpa = calculate_gpa(subjects)
    overall_letter = get_grade_letter(weighted_avg)
    overall_status = get_pass_fail(weighted_avg)

    print(f"Weighted Average : {weighted_avg:.2f}%")
    print(f"Overall Grade    : {overall_letter}")
    print(f"GPA (4.0 Scale)  : {gpa}")
    print(f"Result           : {overall_status}")
    print("=" * 55)

def get_subject_input(subject_num):
    """Gets input for a single subject from the user."""
    print(f"\n--- Subject {subject_num} ---")
    name = input("Enter subject name: ").strip()

    while True:
        try:
            max_marks = float(input("Enter total marks: "))
            if max_marks <= 0:
                print("Total marks must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            marks_obtained = float(input("Enter marks obtained: "))
            if marks_obtained < 0 or marks_obtained > max_marks:
                print(f"Marks must be between 0 and {max_marks}.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            credits = int(input("Enter subject credits (1-5): "))
            if credits < 1 or credits > 5:
                print("Credits must be between 1 and 5.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    percentage = round((marks_obtained / max_marks) * 100, 2)

    return {
        'name': name,
        'marks_obtained': marks_obtained,
        'max_marks': max_marks,
        'credits': credits,
        'percentage': percentage
    }

def main():
    print("=" * 55)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 55)

    student_name = input("Enter student name: ").strip()
    if not student_name:
        student_name = "Unknown Student"

    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects <= 0:
                print("Number of subjects must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    subjects = []
    for i in range(1, num_subjects + 1):
        subject = get_subject_input(i)
        subjects.append(subject)

    print_report(student_name, subjects)

    again = input("\nCalculate for another student? (yes/no): ").strip().lower()
    if again in ['yes', 'y']:
        main()
    else:
        print("\nThank you for using Student Grade Calculator!")

if __name__ == "__main__":
    main()
