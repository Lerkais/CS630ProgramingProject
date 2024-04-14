#4.6.24 4.13.24 4.14.24
#The point of this program is to great a front end for the user to interact with.
import customtkinter #A custom made more updated version of tkinter


def button_event(): #defines action when button is pressed #should work fine as standaline
    if check_var1.get() == "on" or check_var2.get() == "on" or check_var3.get() == "on" or check_var4.get() == "on" or check_var5.get() == "on" or check_var6.get() == "on": #first checks condition if nothing was clicked
        label.configure(text="Please click again to confirm the selected options.") #checks to see if check mark was clicked
        global toLoadAlgorithm
        toLoadAlgorithm = [check_var1.get(), check_var2.get(), check_var3.get(), check_var4.get(), check_var5.get(), check_var6.get()]
        enter_button(eventAction=mainMenu.destroy)
    else:
        label.configure(text="Please select select the appropriate options.")

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

def jobsValue(input): #sliding
    numberOfJobsLabel.configure(text=int(input)) #value getting passed by slider widget
    

def tupleAction(v1= ()):
    print(v1)
    return v1
        
def createMainScreen(): #call this if a program wants the interface
    global check_var1, check_var2, check_var3, check_var4, check_var5, check_var6 #(declares variables so they
    #can communicate with other methods)
    main_window() #generates the main window

    begin_label = customtkinter.CTkLabel(mainMenu, text="Welcome to the Operating System Algorithm Selector.\n To start the program please check the algoritm(s) you would like to test.", font=("Helventica", 18))
    begin_label.pack(pady = 20)

    check_var1 = check_box("FCFS", 20) #first box

    check_var2 = check_box("SRT", 21) #second box

    check_var3 = check_box("RR", 22) #third box

    check_var4 = check_box("SPN", 23) #fourth box

    check_var5 = check_box("HRRN", 24) #fifth box

    check_var6 = check_box("FB", 25) #sixth box

    enter_button() #allows user to send input to be analyzed

    mainMenu.mainloop() #displays main screen and responds to inputs



def arrivalBurstTimeInput():
    arrivalListStorage = []
    burstListStorage = []
    counter = 0
    
    while numberOfJobsInput > counter:
        main_window()
        print(counter)
        arrival_label_input = customtkinter.CTkLabel(mainMenu, text="Please scroll to adjust the arrival time of the job.\nArrival Time:", font=("Helventica", 18))
        arrival_label_input.pack(pady = 20)
        arrivalSlider = customtkinter.CTkSlider(mainMenu, from_=0, to=100, command=arrivalValue)
        arrivalSlider.pack(pady = 25)

        global arrivalLabel
        arrivalLabel = customtkinter.CTkLabel(mainMenu, text=arrivalSlider.get(), font=("Helvetica", 18))
        arrivalLabel.pack(pady = 40)

        burst_label_input = customtkinter.CTkLabel(mainMenu, text="Please scroll to adjust the burst time of the job.\nBurst Time:", font=("Helventica", 18))
        burst_label_input.pack(pady = 55)
        burstSlider = customtkinter.CTkSlider(mainMenu, from_= 1, to=101, command=burstValue)
        burstSlider.pack(pady = 60)

        global burstLabel
        burstLabel = customtkinter.CTkLabel(mainMenu, text=burstSlider.get(), font=("Helvetica", 18))
        burstLabel.pack(pady=65)
        enter_button(eventAction=mainMenu.destroy) #resolve the error codes later
        mainMenu.mainloop()
        arrivalListStorage.append(str(int(arrivalSlider.get())))
        burstListStorage.append(str(int(burstSlider.get())))
        counter += 1
        
    print(arrivalListStorage)
    print(burstListStorage)
    tupleStorageValues = list(zip(arrivalListStorage, burstListStorage))
    print(tupleStorageValues)
    return tupleStorageValues #returns tuple value
    

    #work on tuples later, first get functionality of connecting the two screens
    
    
def numberOfJobs():
    main_window()
    begin_label = customtkinter.CTkLabel(mainMenu, text="Please select the number of jobs you would like to process.\nOnce selected, please press enter to continue.", font=("Helventica", 18))
    begin_label.pack(pady = 20)
    numberOfJobsSlider = customtkinter.CTkSlider(mainMenu, from_=1, to=101, command=jobsValue)
    numberOfJobsSlider.pack(pady = 50)

    global numberOfJobsLabel
    numberOfJobsLabel = customtkinter.CTkLabel(mainMenu, text=numberOfJobsSlider.get(), font=("Helvetica", 18))
    numberOfJobsLabel.pack(pady = 40)
    global numberOfJobsInput
    enter_button(eventAction=mainMenu.destroy)
    mainMenu.mainloop()
    numberOfJobsInput = int(numberOfJobsSlider.get())

#intended order of execution  
#createMainScreen() #modularize beginning label
#numberOfJobs()   #modularize beginning label, (modularize the sliders?)
#arrivalBurstTimeInput() #modularize beginning label, (modularize the sliders?)
 


#things to do: 

#try to modularize the code? (sliders)
#try to make double click a single click
#try to minimize the use of global variables and rely more on returns
#format the windows visuals
#remove debugging code




