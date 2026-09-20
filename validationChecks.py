
def validateIntegerInput(value):
    numberAsInt = None
    try:
        numberAsInt = int(value) #Trying to cast value as an integer
        return numberAsInt #If successful, the integer value is returned
    except ValueError: #If a value error is raised None is returned
        print("This is not an integer")
        return None


def validateValueInput(value,students):
   
    if len(students) == 0:
        print("No values to search here") #If the list is empty, False is returned
        return False
    elif value < 0 or value > len(students): #If the value being searched is out of range, False is returned
        print("Input is out of range")
        return False
    return True


def validateGradeRange(students):
    for i in range(0,len(students)):
        if int(students[i]["grade"]) < 0 or int(students[i]["grade"]>100): #If a grade in the record is out of range, it notifies the teacher
            print("Grade is out of range")
            continue


