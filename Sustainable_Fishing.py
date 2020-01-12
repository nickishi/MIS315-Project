'''
Created on Nov 24, 2019

@author: Nick
'''
import csv
import tkinter
import tkinter.messagebox
import tkinter.ttk

def Reset():
    """Resets each Combobox for the user"""
    global root
    Fish_Box.delete(first = 0, last = 100)
    Year_Box.delete(first = 0, last = 100)
    Waterbody_Box.delete(first = 0, last = 100)
    Month_Box.delete(first = 0, last = 100)

def Exit_B():
    """Exit function for exiting program when button is pressed"""
    global root
    root.destroy()

def Fish_Button():
    """Main function for finding number of fish stocked in the given parameters"""
    
    
    Waterbody_Get = Waterbody_Box.get()  #Retrieves the inputs of the Comboboxes in main program
    Month_Get = Month_Box.get()
    Year_Get = Year_Box.get()
    Fish_Get = Fish_Box.get()
    
    try:
        if Waterbody_Get in Waterbody:        #Each "if" checks for blanks or incorrect input
            Waterbody_Display = Waterbody_Get
        elif Waterbody_Get == "":
            tkinter.messagebox.showerror("Error", "Please select a waterbody.")
            return
        else:
            tkinter.messagebox.showerror("Error", "The waterbody selected does not exist.")
            return
        
        if Month_Get in Month:
            Month_Display = Month_Get
        elif Month_Get == "":
            tkinter.messagebox.showerror("Error", "Please select a month")
            return        
        else:
            tkinter.messagebox.showerror("Error", "Please enter a valid month")
            return
        
        if Year_Get in Year:
            Year_Display = Year_Get 
        elif Year_Get == "":
            tkinter.messagebox.showerror("Error", "Please select a year between 2011 and 2018")
            return
        else:
            tkinter.messagebox.showerror("Error", "Year selected is out of range, \nPlease select a valid year between 2011 and 2018")
            return
        
        if Fish_Get in Fish_Type:
            Fish_Display = Fish_Get
        elif Fish_Get == "":
            tkinter.messagebox.showerror("Error", "Please select a species of fish")
            return  
        else:
            tkinter.messagebox.showerror("Error", "Please enter a valid species of fish")
            return
        
        with open("fish-stocking-lists-actual-beginning-2011.csv","r") as file:
            reader = csv.reader(file) 
            Fish_Grab = int(0)          #Initializes variables used in the count for fish released.
            Fish_Count = int(0)
            Fish_Avg = float(0)
            Fish_Find = int(0)
            Fish_Total_Avg = float(0)
            for row in reader:
                Waterbody_csv = row[2]
                Month_csv = row[4]
                Fish_csv = row[6]
                Year_csv = row[0]
                if Year_Get == Year_csv and Waterbody_Get.lower() == Waterbody_csv.lower() and Month_Get.lower() == Month_csv.lower() and Fish_Get.lower() == Fish_csv.lower():
                    Fish_Grab = int(row[5])
                    Fish_Count += Fish_Grab
                    Fish_Size = float(row[7])     #If parses through each row. If the correct values are found,
                    Fish_Avg += Fish_Size         #then the count is added to the total count.
                    Fish_Find += 1
                    if Fish_Find == 0:
                        Fish_Total_Avg = 0
                    else:
                        Fish_Total_Avg = Fish_Avg / Fish_Find
            
        with open("Search-History.txt", "a") as file:
            file.write("Month: " + Month_Display + "\nYear: " + str(Year_Display) + "\nWaterbody: " + Waterbody_Display +  "\nSpecies: " + Fish_Display + "\nAmount Released: " + str(Fish_Count) + "\nAverage Size: " + str(Fish_Total_Avg) + "\n\n")
        tkinter.messagebox.showinfo("Success!", "Search result saved in Search-History.txt") #Saves search result with the amount of fish released.
    except:
        tkinter.messagebox.showerror("Error", "Unknown error has occurred")  #Error handle if unknown error occurs

    
def main_box():
    """Main function to display program"""
    global root
    global Waterbody_Box  #Variables are global to be used in other functions
    global Year_Box
    global Month_Box
    global Fish_Box 
    
    root = tkinter.Tk()    
    
    root.title("Fish Stocking Application")
    root.geometry("650x80")
    
    Required_Label = tkinter.Label(root, text = "*Required Field")        #Labels and boxes created for their
    Required_Label.grid(row = 0, column = 6)                              #category
    
    Waterbody_Box = tkinter.ttk.Combobox(root, values = Waterbody, width = 25)
    Waterbody_Box.grid(row = 0, column = 1)
    
    Waterbody_Label = tkinter.Label(root, text = "*Waterbody: ")
    Waterbody_Label.grid(row = 0, column = 0)
    
    Fish_Label = tkinter.Label(root, text = "*Fish Type:")
    Fish_Label.grid(row = 0, column = 2)
    
    Fish_Box = tkinter.ttk.Combobox(root, values = Fish_Type, width = 25)
    Fish_Box.grid(row = 0, column = 3)
    
    Year_Label  = tkinter.Label(root, text = "*Year: ")
    Year_Label.grid(row = 1, column = 2)
    
    Year_Box = tkinter.ttk.Combobox(root, values = Year, width = 25)
    Year_Box.grid(row = 1, column = 3)
    
    Month_Box = tkinter.ttk.Combobox(root, values = Month, width = 25)
    Month_Box.grid(row = 1, column = 1)
    
    Month_Label = tkinter.Label(root, text = "*Month: ")
    Month_Label.grid(row = 1, column = 0)
    
    Execute_Button = tkinter.Button(root, text = "Execute", command = Fish_Button)
    Execute_Button.configure(bg = "green")
    Execute_Button.grid(row = 0, column = 5)
    
    Exit_Button = tkinter.Button(root, text = "Exit", command = Exit_B)
    Exit_Button.configure(bg = "red")
    Exit_Button.grid(row = 1, column = 5)
    
    Reset_Button = tkinter.Button(root, text = "Reset", command = Reset)
    Reset_Button.config(bg = "yellow")
    Reset_Button.grid(row = 2, column = 5)
    
    
    root.mainloop()



global Fish_Type
global Year
global Waterbody
global Month
try:
    with open("fish-stocking-lists-actual-beginning-2011.csv","r") as file: #Opens file. Can be adjusted to open
        reader = csv.reader(file)                                           #other files of same format
        
        Waterbody = []
        Month = ["January",   #Months are hard-coded as there are only 12 possible instances
                 "February", 
                 "March", 
                 "April", 
                 "May", 
                 "June", 
                 "July", 
                 "August", 
                 "September",
                 "October",
                 "November",
                 "December"]
        Fish_Type = []
        Year = []
        
        for row in reader:
            Year_Date = str(row[0]) #Pulls data from the .csv
            if Year_Date not in Year and Year_Date != "Year": 
                Year.append(Year_Date)                                   
                                                                #Checks to see if the value is in the list
            Waterbody_Pull = str(row[2])                        #to prevent repeat elements
            if Waterbody_Pull not in Waterbody and Waterbody_Pull != "Waterbody":
                Waterbody.append(Waterbody_Pull)
                Waterbody = sorted(Waterbody)
            
            Fish = str(row[6])
            if Fish not in Fish_Type and Fish != "Species" and Fish != "":
                Fish_Type.append(Fish)
                
    
    main = main_box()
except:
    tkinter.messagebox.showerror("Error", "File could not be found.") #Runs if the file cannot be opened