import unittest
from grade_calculator import (
    get_grade_letter,
    get_grade_points,
    calculate_weighted_average,
    calculate_gpa,
    get_pass_fail
)

class TestGradeCalculator(unittest.TestCase):

    def test_grade_letter_A(self):
        self.assertEqual(get_grade_letter(95), 'A')
        self.assertEqual(get_grade_letter(90), 'A')

    def test_grade_letter_B(self):
        self.assertEqual(get_grade_letter(85), 'B')
        self.assertEqual(get_grade_letter(80), 'B')

    def test_grade_letter_C(self):
        self.assertEqual(get_grade_letter(75), 'C')
        self.assertEqual(get_grade_letter(70), 'C')

    def test_grade_letter_D(self):
        self.assertEqual(get_grade_letter(65), 'D')
        self.assertEqual(get_grade_letter(60), 'D')

    def test_grade_letter_F(self):
        self.assertEqual(get_grade_letter(55), 'F')
        self.assertEqual(get_grade_letter(0), 'F')

    def test_grade_points(self):
        self.assertEqual(get_grade_points('A'), 4.0)
        self.assertEqual(get_grade_points('B'), 3.0)
        self.assertEqual(get_grade_points('C'), 2.0)
        self.assertEqual(get_grade_points('D'), 1.0)
        self.assertEqual(get_grade_points('F'), 0.0)

    def test_pass_fail(self):
        self.assertEqual(get_pass_fail(60), "Pass")
        self.assertEqual(get_pass_fail(75), "Pass")
        self.assertEqual(get_pass_fail(59), "Fail")
        self.assertEqual(get_pass_fail(0), "Fail")

    def test_weighted_average(self):
        subjects = [
            {'percentage': 80, 'credits': 3},
            {'percentage': 70, 'credits': 2},
        ]
        avg = calculate_weighted_average(subjects)
        expected = (80 * 3 + 70 * 2) / 5
        self.assertAlmostEqual(avg, expected)

    def test_gpa_calculation(self):
        subjects = [
            {'percentage': 95, 'credits': 3},
            {'percentage': 85, 'credits': 3},
        ]
        gpa = calculate_gpa(subjects)
        self.assertEqual(gpa, 3.5)

    def test_empty_subjects(self):
        self.assertEqual(calculate_weighted_average([]), 0)
        self.assertEqual(calculate_gpa([]), 0.0)

if __name__ == '__main__':
    unittest.main()
