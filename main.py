from studentRecordManagement import students
from sortByGrade import bubbleSortByGrade, insertionSortByGrade
from searchByID import binarySearch, linearSearch
from validationChecks import validateIntegerInput, validateGradeRange, validateValueInput
from prettytable import PrettyTable

# Importing all the functions from the other file module

class studentRecordManager: #Creating a class to control the main flow of the program
    def __init__(self,students):
        self.students = students # Initalising students

    def outputStudents(self,students): #This function outputs the list of students in a table format
        t = PrettyTable(["ID", "Name", "Grade"]) #PrettyTable library outputs the table in a formatted version 
        for i in range(0,len(students)):
            t.add_row([students[i]['id'], students[i]['student name'], students[i]['grade']])
        print(t)



    def hybridSortSelection(self): #This method is the hybrid sort, allowing the user to pick the sorting method

        while True: # The while loop causes the function to ask for an input again if the user does not enter one of the options
            sortSelection = input(f"Please select the sort you would like to use: \nA) for bubble sort \nB) for insertion sort? ")
            if sortSelection.lower() == "a":
                bubbleSortByGrade(self.students) #Calling the bubble sort function using self.students 
                self.outputStudents(self.students) #Outputting the sorted list of students
                return "\n"

            elif sortSelection.lower() == "b":
                insertionSortByGrade(self.students) #Calling the insertion sort function
                self.outputStudents(self.students) #Outputting the sorted list of students
                return "\n"

            else:
                print(f"Please enter one of the selected options") #Edge case handling to ensure program does not crash
                continue


    def selectSearch(self,students): #This method allows the user or the program to choose which search is implemented

        value = (input("enter the student ID you are searching for: ")) #Asking for student ID that is being searched for
        value = validateIntegerInput(value) #Checking if the value input is a valid integer
        
        if value == None:
            return
        
        if not validateValueInput(value,self.students): #Checking if the value input is within the range of the IDs.
            return
        
        else:
            searchSelection = input(f"To search a student by ID, would you like to \nA) Automatically pick based on the number of students? \nB) Implement Linear Search \nC) Implement Binary Search \n")
            #Asking the user to either select their choice in search, or let the program pick based on the number of students
            if searchSelection.lower() == "b":
                foundIndex = (linearSearch(self.students,value)) #Calling the linear search function
            elif searchSelection.lower() == "c":
                foundIndex = (binarySearch(self.students,value)) #Calling the binary search function
            else:
                print(f"You have either selected A or another character, the search will be automatically chosen")
                if len(self.students) > 40: #If the number of students is greater than 40, binary search will be used
                    foundIndex = (binarySearch(self.students,value))
                else:
                    foundIndex =(linearSearch(self.students,value)) #Linear search is called for a smaller dataset
            student = self.students[foundIndex] #storing the record of the student found as "student"
            self.outputStudents([student]) #Printing the student's details

    def run(self): #This method contains the main flow of the program and the main menu
        
        validateGradeRange(self.students) #Checking if all the grades in the student record are within range.
        students.sort(key = lambda student : int(student["id"]))
        mainMenu = ""
        while mainMenu.lower() != "d": #Continuosly running the program until exit program is selected
            mainMenu = input(f"Please select one of the following: \nA) Display all records \nB) Sort records by grade \nC) Search for record by ID \nD) Exit \nenter your choice here: " )
            if mainMenu.lower() == "a":
                self.outputStudents(self.students) #Outputting the all of student records
            elif mainMenu.lower() == "b": 
                if len(students) <= 1: #Edge case if the record is a single or zero element list, no sorting is required
                    print("No sorting is required")
                else:
                    print(self.hybridSortSelection()) #Calling the hybrid sort method
            elif mainMenu.lower() == "c":
                self.selectSearch(self.students) #Calling the search selection method
            elif mainMenu.lower() == "d":
                print("Exiting the program...") #Terminating the program
                break
            else:
                print(f"This is not one of the options") #Edge case if the wrong input is entered

                    

if __name__ == '__main__':
    manager = studentRecordManager(students)
    manager.run()
