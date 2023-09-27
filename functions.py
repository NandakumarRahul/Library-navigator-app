import csv
import re


classmarks1 = []
classmarks2 = []
subjects = []
locations = []
temp = [] 

try: 
    # the first csv file "classmarkandsub.csv" is read and values of 
    # subjects and classmarks are stored in the lists, subjects and classmarks1 respectively
    with open("classmarkandsub.csv", "r") as file1:
            referance1 = csv.reader(file1)
            for row in referance1:
                subjects.append(row[0].title())
                classmarks1.append(row[1].upper())



    # the second csv file "classmarkandlocation" is read and values of 
    # classmarks and locations are stored in lists, classmarks2 and locations respectievly 
    with open("classmarksandlocation.csv", "r") as file2:
            referance2 = csv.reader(file2)
            for row in referance2:
                classmarks2.append(row[0].upper())
                locations.append(row[1].title())
except IOError:
    print(" ALERT!!!!! check file location")
    exit()

# here a function validate_classmarks is defined,
# which when called takes the user input as arguement 
# #and checks for possible match in list classamrks1 
# and finds its corresponding subject match in list subjects 

def validate_classmarks(classmark):
    for i in range(len(classmarks1)):
        if classmarks1[i] == str(classmark):
            display(i, classmark) 
        # the display function is used in all functions to 
        # initiate printing of the found matching values

# here a function validate_subjects is defined,
# which when called takes the user input as arguement 
# and checks for possible match in list subjects 
# and finds its corresponding classmark match in list classmarks1 

def validate_subjects(subject):
    for i in range(len(subjects)):
         # the search() from re module helps to find the 
         # subject match even when the user has only entered subject part name
        word = re.search(str(subject),str(subjects[i]))
        if word != None: 
            #the value of word would be None if word match is not found
            classmark = classmarks1[i]
            display(i,classmark)
       

# here a function validate_locations is defined,
# which when called takes the user input as arguement 
# and checks for possible match in list locations
# and finds its corresponding classmark match in list classmarks2 

def validate_locations(location):
    for i in range(len(locations)):
        if locations[i] == str(location):
            classmark = classmarks2[i]
            for i in range(len(classmarks1)):
                if classmarks1[i] == classmark:
                    display(i,classmark) 



# the display function when called takes 2 parameters classamrk and an index i
# index i is used to print subject value from list subjects 
# and classmark values passed is used to find corresponding classmark values in lists 
# classmark1 and classmark2 since it is the bridge between the lists subjects and locations

def display(i, classmark):
    for j in range(len(classmarks2)):
        if classmarks2[j] == str(classmark):
            s = f"subject: {subjects[i]} || classmarks: {classmarks1[i].upper()} ||  location: {locations[j]}\n"
            temp.append(s)
''' here instead of printing the value it is stored in a global list temp
    so that it can be called in both the gui version and the consoleversion python file'''