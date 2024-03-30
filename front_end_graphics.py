#3.30.24
#this program may benefit from incorporating classes
#this program may be merged with main.py program
#this program would need someway to only run the algorithms chosen
#other buttons can be added
#import main
import tkinter #use customtkinter
import customtkinter #this one? This one works
#import ttkbootstrap #this one? This one does not work
#from ttkbootstrap.constants import * #more modern version
def loadAlgorithm(): #checkbox function
    print("We will load the value")

def button_event(): #defines action when button is pressed
    if check_var.get() == "on" or check_var2.get() == "on" or check_var3.get() == "on" or check_var4.get() == "on" or check_var5.get() == "on": #first checks condition if nothing was clicked
        print("Button pressed") #test value so far
        label.configure(text="You clicked it") #checks to see if check mark was clicked
        #main.JobDispatcher() #look at how to load the algorithm in
    #eventually want to link with functions from main program
    else:
        label.configure(text="You did not click anything")
        
#def checkbox_event():
#   print("checkbox toggled, current value ", check_var.get())

mainMenu = customtkinter.CTk() #creates main Menu window
mainMenu.geometry("800x600") #defines size of the window
mainMenu.title("Algorithm Selector")

check_var = customtkinter.StringVar(value = "off") #custom string
check1 = customtkinter.CTkCheckBox(mainMenu, text="Algorithm 1", variable=check_var, #label 1
                                    onvalue="on", offvalue="off", command=loadAlgorithm,
                                    fg_color = "blue")
check1.pack(pady=20) #first box

check_var2 = customtkinter.StringVar(value = "off") #custom string
check2 = customtkinter.CTkCheckBox(mainMenu, text="Algorithm 2", variable=check_var2, #label 2
                                    onvalue="on", offvalue="off", command=loadAlgorithm,
                                    fg_color = "blue")
check2.pack(pady=24) #second box

check_var3 = customtkinter.StringVar(value = "off") #custom string
check3 = customtkinter.CTkCheckBox(mainMenu, text="Algorithm 3", variable=check_var3, #label 3
                                    onvalue="on", offvalue="off", command=loadAlgorithm,
                                    fg_color = "blue")
check3.pack(pady=28) #third box

check_var4 = customtkinter.StringVar(value = "off") #custom string
check4 = customtkinter.CTkCheckBox(mainMenu, text="Algorithm 4", variable=check_var4, #label 4
                                    onvalue="on", offvalue="off", command=loadAlgorithm,
                                    fg_color = "blue")
check4.pack(pady=32) #fourth box

check_var5 = customtkinter.StringVar(value = "off") #custom string
check5 = customtkinter.CTkCheckBox(mainMenu, text="Algorithm 5", variable=check_var5, #label 5
                                    onvalue="on", offvalue="off", command=loadAlgorithm,
                                    fg_color = "blue")
check5.pack(pady=36) #fifth box


#save label for if user does not press anything
label =customtkinter.CTkLabel(mainMenu, text="")
label.pack(pady=60)




enter = customtkinter.CTkButton(master=mainMenu, text = "Enter", command=button_event) #main button user presses when they want to enter
enter.place(relx=0.5, rely=.9, anchor=customtkinter.CENTER) #defines where the button goes




mainMenu.mainloop() #displays main screen



#create app class then possibly create top level class (2 different windows)



#code from CustomTkinter CTk example code

#button
