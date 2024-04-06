#4.6.24
#The point of this program is to great a front end for the user to interact with.
import customtkinter #A custom made more updated version of tkinter

def button_event(): #defines action when button is pressed #should work fine as standaline
    if check_var1.get() == "on" or check_var2.get() == "on" or check_var3.get() == "on" or check_var4.get() == "on" or check_var5.get() == "on" or check_var6.get() == "on": #first checks condition if nothing was clicked
        label.configure(text="You clicked something!") #checks to see if check mark was clicked
    else:
        label.configure(text="You did not click anything.")

def main_window(dimensions = "800x600", top_Title = "Algorithm Selector"):
    global mainMenu
    mainMenu = customtkinter.CTk() #creates main Menu window
    mainMenu.geometry(dimensions) #defines size of the window
    mainMenu.title(top_Title)

def check_box(text_input = "Algorithm", pady=20):
    global check_var
    check_var = customtkinter.StringVar(value = "off") #custom string
    check = customtkinter.CTkCheckBox(mainMenu, text=text_input, variable=check_var, #label 1
                                    onvalue="on", offvalue="off", #command can be used to link to which ever algorithm we want
                                    fg_color = "blue")
    check.pack(pady=pady) #first box
    return check_var

def enter_button(button_label = "Enter", relx = 0.5, rely = .9, pady = 60, eventAction = button_event):
    global label
    enter = customtkinter.CTkButton(master=mainMenu, text = button_label, command=eventAction) #main button user presses when they want to enter
    enter.place(relx=relx, rely=rely, anchor=customtkinter.CENTER) #defines where the button goes
    label = customtkinter.CTkLabel(mainMenu, text="")
    label.pack(pady=pady)

def arrivalValue(input): #sliding
    arrivalLabel.configure(text=int(input)) #value getting passed by slider widget

def burstValue(input):
    burstLabel.configure(text=int(input))

def tupleAction(v1= ()):
    print(v1)
    return v1
        
def createMainScreen(): #call this if a program wants the interface
    global check_var1, check_var2, check_var3, check_var4, check_var5, check_var6 #(declares variables so they
    #can communicate with other methods)

    main_window() #generates the main window

    check_var1 = check_box("FCFS", 20) #first box

    check_var2 = check_box("SRT", 21) #second box

    check_var3 = check_box("RR", 22) #third box

    check_var4 = check_box("SPN", 23) #fourth box

    check_var5 = check_box("HRRN", 24) #fifth box

    check_var6 = check_box("FB", 25) #sixth box

    enter_button() #allows user to send input to be analyzed

    mainMenu.mainloop() #displays main screen and responds to inputs

def arrivalBurstTimeInput():
    main_window()
    arrivalSlider = customtkinter.CTkSlider(mainMenu, from_=0, to=100, command=arrivalValue)
    arrivalSlider.pack(pady = 20)
    global arrivalLabel
    arrivalLabel = customtkinter.CTkLabel(mainMenu, text=arrivalSlider.get(), font=("Helvetica", 18))
    arrivalLabel.pack(pady = 40)
    arrivalSlider.set(0)



    burstSlider = customtkinter.CTkSlider(mainMenu, from_= 0, to=100, command=burstValue)
    burstSlider.pack(pady = 60)
    global burstLabel
    burstLabel = customtkinter.CTkLabel(mainMenu, text=burstSlider.get(), font=("Helvetica", 18))
    burstLabel.pack(pady=70)
    burstSlider.set(0)
    #tupleStorage = (arrivalSlider.get(), burstSlider.get()) #work on tuples later, first get functionality of connecting the two screens
    enter_button(eventAction=mainMenu.destroy) #resolve the error codes later
    mainMenu.mainloop()
    

#revise mainMenu to something else unique to the first tab to see if errors can be avoided
#arrivalBurstTimeInput() #work on modularizing it and making two separate #when trying to run back to back, creates weird text in terminal
#createMainScreen()
#createMainScreen()


