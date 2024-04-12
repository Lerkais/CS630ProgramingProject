#Revising it so that it is more stable
#4.12.24 #burst time #arrival time # which algorithms #how many jobs 
#The point of this program is to great a front end for the user to interact with.
import customtkinter #A custom made more updated version of tkinter

def main_window(theRoot, dimensions = "800x600", top_Title = "Algorithm Selector"):
    theRoot = customtkinter.CTk() #creates main Menu window (Does not make sense)
    theRoot.geometry(dimensions) #defines size of the window
    theRoot.title(top_Title)

def check_box(theRoot, text_input = "Algorithm", pady=20):
    check_var = customtkinter.StringVar(value = "off") #custom string
    check = customtkinter.CTkCheckBox(theRoot, text=text_input, variable=check_var, #label 1
                                    onvalue="on", offvalue="off", #command can be used to link to which ever algorithm we want
                                    fg_color = "blue")
    check.pack(pady=pady) #first box
    return check_var

def button_event(theRoot): #defines action when button is pressed #should work fine as standaline
    if check_var1.get() == "on" or check_var2.get() == "on" or check_var3.get() == "on" or check_var4.get() == "on" or check_var5.get() == "on" or check_var6.get() == "on": #first checks condition if nothing was clicked
        print("Yes")
        #confirmationLabel = customtkinter.CTkLabel(master= theRoot)
        #confirmationLabel.configure(text="You clicked something!") #checks to see if check mark was clicked
        #global toLoadAlgorithm
        #toLoadAlgorithm = [check_var1.get(), check_var2.get(), check_var3.get(), check_var4.get(), check_var5.get(), check_var6.get()]
        #returns contents for telling which algorithms to load
    else: 
        print("No")

def enter_button(theRoot, button_label = "Enter", relx = 0.5, rely = .9, pady = 60): #eventAction = button_event
    enter = customtkinter.CTkButton(master=theRoot, text = button_label) #command=eventAction#main button user presses when they want to enter
    enter.place(relx=relx, rely=rely, anchor=customtkinter.CENTER) #defines where the button goes
    label = customtkinter.CTkLabel(theRoot, text="Test")
    label.pack(pady=pady)
'''

def arrivalValue(input): #sliding
    arrivalLabel.configure(text=int(input)) #value getting passed by slider widget

def burstValue(input):
    burstLabel.configure(text=int(input))
'''
def createMainScreen(): #call this if a program wants the interface
    global check_var1, check_var2, check_var3, check_var4, check_var5, check_var6 #(declares variables so they
    #can communicate with other methods)

    mainMenuReal = customtkinter.CTk() #creates main Menu window
    mainMenuReal.geometry("800x600") #defines size of the window
    mainMenuReal.title("Algorithms")
    begin_label = customtkinter.CTkLabel(mainMenuReal, text="Welcome to the Operating System Algorithm Selector.\n To start the program please check the algoritm(s) you would like to test.", font=("Helventica", 18))
    begin_label.pack(pady = 20)

    check_var1 = check_box(mainMenuReal, "FCFS", 20) #first box

    check_var2 = check_box(mainMenuReal, "SRT", 21) #second box

    check_var3 = check_box(mainMenuReal, "RR", 22) #third box

    check_var4 = check_box(mainMenuReal, "SPN", 23) #fourth box

    check_var5 = check_box(mainMenuReal, "HRRN", 24) #fifth box

    check_var6 = check_box(mainMenuReal, "FB", 25) #sixth box

    enter_button(mainMenuReal) #allows user to send input to be analyzed #executes for no reason 

    mainMenuReal.mainloop() #displays main screen and responds to inputs
'''''
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
    enter_button(eventAction = mainMenu.destroy) #resolve the error codes later
    mainMenu.mainloop()
    global tupelStorage
    tupleStorage = (int(arrivalSlider.get()), int(burstSlider.get())) #work on tuples later, first get functionality of connecting the two screens
    print(tupleStorage) #for error checking
    '''
    

#revise mainMenu to something else unique to the first tab to see if errors can be avoided

#work on modularizing it and making two separate #when trying to r
createMainScreen()
#print(toLoadAlgorithm)
#print(toLoadAlgorithm)
#we got list and tuple to store data. 
#(There is a glitch where removing one tab leaves some processes running causing
#intrepreter to not like it. Additionally, there should be a way to use alternative methods
#other than global and using different mainMenu option as that seems to cause issues)
#This issue is not program crashing and the program works
#but can cause instability in the program.
