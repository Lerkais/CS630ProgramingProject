#4.4.24
#The point of this program is to great a front end for the user to interact with.
import customtkinter #A custom made more updated version of tkinter

def button_event(): #defines action when button is pressed #should work fine as standaline
    if check_var1.get() == "on" or check_var2.get() == "on" or check_var3.get() == "on" or check_var4.get() == "on" or check_var5.get() == "on": #first checks condition if nothing was clicked
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

def enter_button(button_label = "Enter", relx = 0.5, rely = .9, pady = 60):
    global label
    enter = customtkinter.CTkButton(master=mainMenu, text = button_label, command=button_event) #main button user presses when they want to enter
    enter.place(relx=relx, rely=rely, anchor=customtkinter.CENTER) #defines where the button goes
    label = customtkinter.CTkLabel(mainMenu, text="")
    label.pack(pady=pady)
        
def createMainScreen(): #call this if a program wants the interface
    global check_var1, check_var2, check_var3, check_var4, check_var5 #(declares variables so they
    #can communicate with other methods)

    main_window() #generates the main window

    check_var1 = check_box("FCFS", 20) #first box

    check_var2 = check_box("SRT", 24) #second box

    check_var3 = check_box("RR", 28) #third box

    check_var4 = check_box("SPN", 32) #fourth box

    check_var5 = check_box("HRRN", 36) #fifth box

    enter_button() #allows user to send input to be analyzed

    mainMenu.mainloop() #displays main screen and responds to inputs
