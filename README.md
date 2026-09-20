# StudentRecordLookupSystem
Student record system implementing core fundamentals of algorithms and data structures.

WM180-5680156
Project Overview
This program implements a Student Record Lookup System demonstrating bubble sort, insertion sort, linear search and binary search.
Features Implemented
Sorting Algorithms:
All sorts sort the student records in descending order by grade:

Bubble Sort
Insertion Sort
Hybrid Sort (Choice based algorithm to pick between bubble and insertion sort)

Searching Algorithms:
All searching algorithms search for a student by ID:
Linear Search
Binary Search

Additional Features:

Grade Validation
Handling duplicate grades
Edge case handling

Dependancies
The external modules required to run the program include:

'unittest'
'PrettyTable'

Installation

clone the repository by using "git clone https://mygit.wmg.warwick.ac.uk/u5680156/wm180-5680156/-/tree/de0eb66d1b650dd898b7531155c7fa5793813abc/](https://github.com/hannahhemnani-source/StudentRecordLookupSystem.git "
ensure all files are stored within the same folder

Running ByteBridge - File Paths
This project uses relative paths, meaning that it must be run from the repository root folder, otherwise Python will look for files in the wrong place.
The expected folder structure is displayed below
WM180_5680156/
main.py
searchByID.py
sortByGrade.py
studentRecordManagement.py
testByteBridge.py
validationChecks.py
Executing the program
How to run the program:

Open the command prompt/terminal
Ensure you are in the repository root directory
Run "python3 main.py"

Running unit tests:
Unit tests are implemented by using the unittest module in Python. To run testByteBridge.py, ensure it is in the same folder as the other python files and run "python3 -m unittest testByteBridge.py"
These tests validate:

Bubble sort
Insertion sort
Linear Search
Binary Search
Validation functions

Help
To exit the program early, use Ctrl + C or Ctrl + Z
If encountering:

Python command not found, try using python3 instead.
