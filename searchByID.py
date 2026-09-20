
def binarySearch(students,value):
    foundIndex = -1 
    # sets the found index as -1 as the index hasnt been found yet
    valueFound = False #setting found value as false
    first = 0
    last = len(students) - 1
    while first<=last and valueFound != True:
        midValue = (first+last)//2 #defining the midpoint
        foundIndex = midValue
        if value == students[midValue]["id"]:
            valueFound = True #If value is found the program stops and returns the found index
        elif value > students[midValue]["id"] :
            first = midValue + 1 
            # redefines first to be the next value after the mid point of the list 
        elif value < students[midValue]["id"]:
            last = midValue - 1
            # redefines the last in the list to be the value below the midpoint
    if valueFound == False:
        print("Value not found")
        foundIndex = -1
    return foundIndex
    

def linearSearch(students,value):
    foundIndex = -1
    valueFound = False
    while valueFound !=True and foundIndex < len(students)-1: #Iterating through the list until value is found or end of list is reached
        foundIndex += 1
        if students[foundIndex]["id"] == value:
            valueFound = True #Checking if current index matches the value being searched
    if valueFound == False:
        print("ID not found")
        foundIndex = -1
    return foundIndex
    

    
