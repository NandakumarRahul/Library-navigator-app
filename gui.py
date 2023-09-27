import tkinter as tk
import functions as fn


interface = tk.Tk()

interface.geometry("800x1000")              
# defining the size of the gui window
interface.minsize(800,1000)                 
# minimum size of window
interface.maxsize(800,1000)                 
# maximum size of window

interface.title('Library Navigator')        
# making the title as library navigator

#place() is used in this program to facilitate placement of every element in gui

# the function getsub accesses the textvariable of subjectentry 
# and passes it to validate_subjects functions 
# and prints the matching subject, classmark and location
def button1():
    def getsub():
        temp = subjectvalue.get()           
        # the userinput is accessed
        fn.validate_subjects(temp.title())  
        # userinput is validated
        output =  ' '
        for i in fn.temp: 
            # if the userinput matches any subject,
            # the values will be stored in temp list in functions.py which is accessed here
            output += str(i)
        result.config(text = str(output))   
        # updates the result labels text to the matching results
    tk.Label(interface, text = "------------------------------------------------------------YOU SELECTED OPTION SUBJECTS------------------------------------------------------------").place(x = 0, y = 150)
    subject = tk.Label(interface, text = "Subject name or part name").place(x = 200, y = 175)
    subjectvalue = tk.StringVar() 
    # initialises the value to be a string
    subjectentry = tk.Entry(interface, textvariable = subjectvalue).place(x = 400, y = 175) 
    # creates a textbox for user to input values
    tk.Button(text = "submit", command = getsub).place(x = 550, y = 175)
    result = tk.Label(interface, text = " ")
    result.place(x=220,y=220)

    

# the function getclass accesses the textvariable of classmarkentry 
# and passes it to validate_classmarks functions 
# and prints the matching subject, classmark and location
'''working is same as button1() 
   but here the user input is classmarkvalue'''
def button2():
    def getclass():
        temp = classmarkvalue.get()
        fn.validate_classmarks(temp.upper())
        output =  ' '
        for i in fn.temp:
            output += str(i)
        result.config(text = str(output))
    tk.Label(interface, text = "------------------------------------------------------------YOU SELECTED OPTION CLASSMARKS------------------------------------------------------------").place(x = 0, y = 150)
    classmark = tk.Label(interface, text = "Classmark").place(x = 200, y = 175)
    classmarkvalue = tk.StringVar()
    classmarkentry = tk.Entry(interface, textvariable= classmarkvalue).place(x = 400, y = 175)
    tk.Button(text = "submit", command = getclass).place(x = 550, y = 175)
    result = tk.Label(interface, text = " ")
    result.place(x=220,y=220)



# the function getloc accesses the listbox selected value 
# and passes it to validate_locations functions 
# and prints the matching subject, classmark and location

def button3():
    def getloc():
        cs = locbox.curselection()[0]
        temp = locbox.get(cs)
        fn.validate_locations(temp.title())
        output =  ' '
        for i in fn.temp:
            output += str(i)
        result.config(text = str(output))
    tk.Label(interface, text = "------------------------------------------------------------YOU SELECTED OPTION LOCATIONS------------------------------------------------------------").place(x = 0, y = 150)
    location = tk.Label(interface, text = "Location").place(x = 200, y = 175)
    locbox = tk.Listbox(interface,height=6)
    # listbox is created 
    locbox.place(x=400, y= 175)
    locbox.insert(0, "Top Floor Front Right") 
    # inserting values into listboc
    locbox.insert(0, "Top Floor Back Right")
    locbox.insert(0, "Top Floor Front Left")
    locbox.insert(0, "Top Floor Back Left")
    locbox.insert(0, "Ground Floor")
    locbox.insert(0, "Middle Floor")
    result = tk.Label(interface, text = " ")
    result.place(x=220,y=272)
    locbox.bind('<<ListboxSelect>>', lambda x: getloc())
    # using getloc function to carry out validation and print value
    


# here tk.label is used to present texts and headings in gui
tk.Label(interface, text ="Welcome to library Navigator", font="timenewroman 12  bold").place(x=250, y = 5)
tk.Label(interface, text = "please select any of the three options given").place(x = 240, y = 30)

# here tk.button is used to prompt user to select any one option by clicking any button
tk.Button(text = "Subjects", command = button1).place(x = 325, y = 55)
tk.Button(text = "Classmarks", command = button2).place(x = 315, y = 85)
tk.Button(text = "Locations", command = button3).place(x = 320, y = 115)
# each button is linked to button1, button2 or button3

interface.mainloop()


