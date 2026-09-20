import unittest
from studentRecordManagement import students
from sortByGrade import bubbleSortByGrade, insertionSortByGrade
from searchByID import linearSearch,binarySearch
from validationChecks import validateGradeRange,validateIntegerInput,validateValueInput


class testByteBridge(unittest.TestCase):


    def testBubbleSort(self):
        students = [
        {"id": 30, "student name": "Sebastiano", "grade": 84},
        {"id": 31, "student name": "Christian", "grade": 69},
        {"id": 32, "student name": "Dante", "grade": 20},
        {"id": 33, "student name": "Alex", "grade": 63},
        {"id": 34, "student name": "Justin", "grade": 23},
        ]

        sorted_students = bubbleSortByGrade(students)

        self.assertEqual(sorted_students[0]["grade"],84)
        self.assertEqual(sorted_students[1]["grade"],69)
        self.assertEqual(sorted_students[2]["grade"],63)
        self.assertEqual(sorted_students[3]["grade"],23)
        self.assertEqual(sorted_students[4]["grade"],20)


    def testInsertionSort(self):
        students = [
        {"id": 30, "student name": "Sebastiano", "grade": 84},
        {"id": 31, "student name": "Christian", "grade": 69},
        {"id": 32, "student name": "Dante", "grade": 20},
        {"id": 33, "student name": "Alex", "grade": 63},
        {"id": 34, "student name": "Justin", "grade": 23},
        ]

        sorted_students = insertionSortByGrade(students)

        self.assertEqual(sorted_students[0]["grade"],84)
        self.assertEqual(sorted_students[1]["grade"],69)
        self.assertEqual(sorted_students[2]["grade"],63)
        self.assertEqual(sorted_students[3]["grade"],23)
        self.assertEqual(sorted_students[4]["grade"],20)


    def testLinearSearch(self):
        students = [
        {"id": 30, "student name": "Sebastiano", "grade": 84},
        {"id": 31, "student name": "Christian", "grade": 69},
        {"id": 32, "student name": "Dante", "grade": 20},
        {"id": 33, "student name": "Alex", "grade": 63},
        {"id": 34, "student name": "Justin", "grade": 23},
        ]

        value1 = 34
        value2 = 70
        
        foundIndex1 = linearSearch(students,value1)
        foundIndex2 = linearSearch(students, value2)
        self.assertEqual(students[foundIndex1]["grade"],23)
        self.assertEqual(foundIndex2,-1)



    def testBinarySearch(self):
        students = [
        {"id": 34, "student name": "Justin", "grade": 23},
        {"id": 30, "student name": "Sebastiano", "grade": 84},
        {"id": 31, "student name": "Christian", "grade": 69},
        {"id": 33, "student name": "Alex", "grade": 63},
        {"id": 32, "student name": "Dante", "grade": 20}
        ]
        students.sort(key = lambda student : int(student["id"]))
        value1 = 32
        value2 = 44
        foundIndex1 = binarySearch(students,value1)
        foundIndex2 = binarySearch(students,value2)
        self.assertEqual(students[foundIndex1]["grade"],20)
        self.assertEqual(foundIndex2,(-1))


    def testValidationChecks(self):
        value1 = "TestValue"
        value2 = 5
        value3 = 3000
        students = [{"id": 1, "student name": "Alex", "grade": 63},
        {"id": 1, "student name": "Dante", "grade": 20},{"id": 3, "student name": "Freya", "grade": 89},
    {"id": 4, "student name": "Ishita", "grade": 100},
    {"id": 5, "student name": "Nikhita", "grade": 67},
    {"id": 6, "student name": "Jack", "grade": 58}]
        studentsEmpty = []
        studentsRange = [{"id": 33, "student name": "Alex", "grade": 63},
        {"id": 32, "student name": "Dante", "grade": 120}] 

        testIntInput1 = validateIntegerInput(value1)
        testIntInput2 = validateIntegerInput(value2)
        testValInput1 = validateValueInput(value3,students)
        testValInput2 = validateValueInput(value2,studentsEmpty)
        testValInput3 = validateValueInput(value2,students)
        testGradeInput = validateGradeRange(studentsRange)
        print(testValInput3)

        self.assertEqual(testIntInput1,None)
        self.assertEqual(testIntInput2,5)
        self.assertEqual(testValInput1,False)
        self.assertEqual(testValInput2,False)
        self.assertEqual(testValInput3,True)
        self.assertEqual(testGradeInput,None)






if __name__ == '__main__':
    unittest.main()
