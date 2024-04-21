#4.19.24
#The point of this program is to great a front end for the user to interact with.
import customtkinter #A custom made more updated version of tkinter
import time #for sleep()

def button_event(): #defines action when button is pressed #should work fine as standaline
    if check_var1.get() == "on" or check_var2.get() == "on" or check_var3.get() == "on" or check_var4.get() == "on" or check_var5.get() == "on" or check_var6.get() == "on": #first checks condition if nothing was clicked
        label.configure(text="Please click again to confirm the selected options.") #checks to see if check mark was clicked
        global toLoadAlgorithm
        toLoadAlgorithm = [check_var1.get() == "on", check_var2.get() == "on", check_var3.get() == "on", check_var4.get() == "on", check_var5.get() == "on", check_var6.get() == "on"]
        #enter_button(eventAction=mainMenu.destroy) #find way to make it 1 click
        #mainMenu.withdraw()
        #mainMenu.quit()
        mainMenu.destroy()
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
    main_window("800x600") #generates the main window

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
    

jobretlist = []
numberOfJobsInput = 0
arrivalVar = None
burstVar = None
arrivalValue = 0
burstValue = 0
arrburLabel = ""
def tracerGetJob():
    global arrivalValue, burstValue,arrivalEntry, burstEntry,arrburLabel
    arrivalValue = arrivalEntry.get()
    burstValue = burstEntry.get()
    #arrburLabel = "Arr/burst: "+ str(arrivalValue) + "/" + str(burstValue)
    #print(arrburLabel)

def editedArrivalBurstTimeInput():
    global numberOfJobsInput

    for i in range(numberOfJobsInput): #loop to get the jobs input
        jobretlist.append(getJob(i))
        
    return jobretlist
   
def errorHandlerCode(): #for handling if user tries to enter a negative number or any character not a number
    main_window("600x400", "Error Condition")
    begin_label = customtkinter.CTkLabel(mainMenu, 
        text="Since an invalid character\nwas attempted to be entered,\n this program needs to be restarted.\nPlease close this window and\n press the enter button on the other tab."
        , font=("Helventica", 28))
    begin_label.pack(pady = 20)
    mainMenu.mainloop()
    exit()

def getJob(i): #function to get job through tkinter graphics window seperate from arrivalBurstTimeInput using text entry boxes
    global arrivalValue, burstValue
    global arrivalEntry, arrivalVar
    global burstEntry, burstVar
    checker = 0
    lock = 0
    while lock == 0:
        main_window()
        job_label = customtkinter.CTkLabel(mainMenu, text="Please enter the arrival time and burst time for job "+str(i+1)+".\nArrival Time:", font=("Helventica", 18))
        job_label.pack(pady = 20)
        arrivalVar = customtkinter.StringVar()
        arrivalEntry = customtkinter.CTkEntry(mainMenu,textvariable=arrivalVar)
        arrivalEntry.pack(pady = 40)
        burst_label = customtkinter.CTkLabel(mainMenu, text="Burst Time:", font=("Helventica", 18))
        burst_label.pack(pady = 40)
        burstVar = customtkinter.StringVar()
        burstEntry = customtkinter.CTkEntry(mainMenu,textvariable=burstVar)
        burstEntry.pack(pady = 80)
        arrivalVar.trace("w", lambda *args: tracerGetJob())
        burstVar.trace("w", lambda *args: tracerGetJob())
        enter_button(eventAction=mainMenu.destroy)
        mainMenu.mainloop()
        try: 
            checker = int(arrivalValue) #if values entered cannot work with int
            checker = int(burstValue) #then the user is reprompted
            if int(arrivalValue) < 0: #if user enters int that does not make sense, program #CAN BE 0 
                arrivalValue = "1" #assumes the user meant 1
            if int(burstValue) <= 0:
                burstValue = "1"
            return int(arrivalValue), int(burstValue) #if works value returns
        except: #if does not work, reset loop until user complies
            lock = 0 #results in loop to repeat again

numJobsVar = None
numJobs = 0
numjobs =None


 

def numberOfJobsEntry(): #same as slider but with text entry
    main_window()
    global numJobsVar, numJobs,numjobs
    numJobsVar = customtkinter.StringVar()

    begin_label = customtkinter.CTkLabel(mainMenu, text="Please enter the number of jobs you would like to process.\nOnce entered, please press enter to continue.", font=("Helventica", 18))
    begin_label.pack(pady = 20)
    numjobs = customtkinter.CTkEntry(mainMenu,textvariable=numJobsVar) #put logic to handle invalid inputs
    numjobs.pack(pady = 40)
    
    
    def tracerNumJobs(*args):
        global numJobs
        value = numJobsVar.get()
        print("Value:", value)
        try:
            numJobs = int(value)
        except ValueError:
            print("Invalid input:", value)

    numJobsVar.trace_add("write", tracerNumJobs)
    
    def enterButton():
        try:
            numJobs = numjobs.get() #tries to run the code
        except ValueError: #if user tries to enter anything other than a number the program will end #can back space if not bank
            #errorHandlerCode() #cannot be tested because whenever user enters a character and enters, the program runs default values
            print("Error")
        mainMenu.destroy()

    enter_button(eventAction=lambda *args: enterButton()) 
    mainMenu.mainloop()



    print("numjobs: ", numJobs)
    return numJobs
    



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
    
