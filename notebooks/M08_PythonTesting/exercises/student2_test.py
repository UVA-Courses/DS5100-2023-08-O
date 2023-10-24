from student2 import Student
import unittest

class EnrollInTestCase(unittest.TestCase): 
    
    def test_01_is_numCoursincremented_correctly(self):
        student1 = Student('Katherine', ['DS 5100'])
        student1.enroll_in_course("CS 5050")
        student1.enroll_in_course("CS 5777")        
        expected = 3
        actual = student1.num_courses
        self.assertEqual(actual, expected)
        
    def test_02_is_course_removed(self):
        student1 = Student('Katherine', ['DS 5100'])
        course = "CS 5050"
        student1.enroll_in_course(course)
        student1.unenroll_in_course(course)
        self.assertFalse(course in student1.courses)

    def test_03_is_course_not_added(self):
        student1 = Student('Katherine', ['DS 5100'])
        expected = len(student1.courses)
        course = "CS 5050"
        student1.unenroll_in_course(course)
        actual = len(student1.courses)
        self.assertEqual(actual, expected)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
