import functions as fn                
# importing the functions.py file to 
# use the functions defined in it to validate the user input

option = int(input("please select any of the given options as 1, 2 or 3:\n 1: Subjects \n 2: Classmarks \n 3: Locations\n "))
if option == 1:
    print(fn.subjects)
    subject = input("please enter your subject name or part name from above list: ").title()
    # using title function to get rid of any user capitalization errors
    fn.validate_subjects(subject)     
    # using the validate_subjects function from functions.py to 
    # check for any possible subject match to the user input
    for i in fn.temp:                 
        # printing the matching subject, location and classmark values stored in the list temp
        print(i, '\n')

elif option == 2:
    print(fn.classmarks2)
    classmark = input("please enter your preferred classmark from above list: ").upper()
    fn.validate_classmarks(classmark)
    # using the validate_classmarks function from functions.py to 
    # check for any possible classmark match to the user input
    for i in fn.temp:                 
        print(i, '\n')
        
elif option ==3:
    print("1: Top Floor Front Right")
    print("2: Top Floor Back Right ")
    print("3: Top Floor Back Left")
    print("4: Top Floor Front Left")
    print("5: Ground Floor")
    print("6: Middle Floor")
    
    location = input("enter the preferred location from above list : ").title()
    fn.validate_locations(location)   
    for i in fn.temp:
        print(i, '\n')
