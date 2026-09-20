
def bubbleSortByGrade(students):
    swapped = True
# sets swapped to true as the base case
    while swapped == True:
    # makes swapped false so when a pass is completed with no swaps the sort stops
        swapped = False
        for item in range(0,len(students)-1):
            if students[item]["grade"]< students[item+1]["grade"]: #swapping the values if they are in the wrong order
                temp = students[item]
                students[item] = students[item+1]
                students[item+1] = temp
                swapped = True
    return students #The code stops when a pass is completed where no swaps are made and swapped is set to false.


def insertionSortByGrade(students):
    for index in range (1,len(students)):
        insertItem = students[index] #Storing the item currently being inserted
        index = index - 1
        while index >=0 and insertItem["grade"] > students[index]["grade"]: #Comparing the item to the sorted list and shifting them while they are smaller
            students[index+1] = students[index]
            index = index - 1
        students[index+1] = insertItem #Inserting the item into the correct, sorted position
    return students



