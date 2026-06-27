# Student Grade Calculator 🎓

A simple Python command-line application to calculate student grades, weighted averages, and GPA based on subject marks and credits.

## Features

- Enter marks for multiple subjects with individual credit weights
- Calculates percentage per subject
- Assigns letter grades (A, B, C, D, F)
- Computes weighted average across all subjects
- Calculates GPA on a 4.0 scale
- Shows Pass/Fail status per subject and overall
- Prints a clean formatted grade report

## How to Run

Make sure you have Python 3 installed.

```bash
python grade_calculator.py
```

## Sample Output

```
=======================================================
         STUDENT GRADE REPORT
=======================================================
Student Name : Rajakhunnisa Shaik
-------------------------------------------------------
Subject              Marks      %  Grade   Status
-------------------------------------------------------
Mathematics         85/100  85.0%      B     Pass
Physics             78/100  78.0%      C     Pass
Programming in C    92/100  92.0%      A     Pass
English             70/100  70.0%      C     Pass
Electronics         88/100  88.0%      B     Pass
-------------------------------------------------------
Weighted Average : 83.47%
Overall Grade    : B
GPA (4.0 Scale)  : 3.16
Result           : Pass
=======================================================
```

## Grade Scale

| Percentage | Letter Grade | Grade Points |
|------------|-------------|--------------|
| 90 - 100   | A           | 4.0          |
| 80 - 89    | B           | 3.0          |
| 70 - 79    | C           | 2.0          |
| 60 - 69    | D           | 1.0          |
| Below 60   | F           | 0.0          |

## Running Tests

```bash
python test_grade_calculator.py
```

## Project Structure

```
student-grade-calculator/
├── grade_calculator.py       # Main application
├── test_grade_calculator.py  # Unit tests
├── sample_data.py            # Example inputs and outputs
└── README.md                 # Project documentation
```

## Technologies Used

- Python 3
- unittest (built-in testing library)

## Author

Rajakhunnisa Shaik
