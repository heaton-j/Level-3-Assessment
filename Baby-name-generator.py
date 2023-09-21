import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

# opening name file from drive

myfile = open("G:\My Drive\Digital Science\Level-3-Assessment/Names.txt","r")
lines = myfile.readlines()

# removing newline from names

lines = [x.strip() for x in lines]

# opening line for users in the terminal

opening_text =["", "Your names will show here when all fields are correctly "
                "filled :",""]

for text in opening_text:
    print(text)


# creating main gui frame

window = tk.Tk()

window.rowconfigure([0, 1, 2, 3], minsize=130, weight=1)
window.columnconfigure([0, 1, 2], minsize=200, weight=1)

# Important titles for generator

main_title = tk.Label(text="Baby Name Generator", width=18, height=6,
                        font=('Times', 20))
main_title.grid(row=0, column=1)


# background frame for gender option

gender_frame = tk.Frame(master=window, bg="lightblue")
gender_frame.grid(row=1, column=1, sticky="nsew")


# background frame for number option

number_frame = tk.Frame(master=window, bg="lightpink")
number_frame.grid(row=2, column=1, sticky="nsew")



# function for print statement for the names

# main function to print the names 

def print_name3(user_gender, user_number):
    user_gender = gender_entry.get()
    user_number = number_entry.get()
    if user_gender =="Girl" and user_number == "1":
        print(lines[1])
    if user_gender =="Girl" and user_number =="2":
        print(lines[1:3])
    if user_gender =="Girl" and user_number =="3":
        print(lines[1:4])
    if user_gender =="Girl" and user_number =="4":
        print(lines[1:5])
    if user_gender =="Girl" and user_number =="5":
        print(lines[1:6])
    if user_gender =="Girl" and user_number =="6":
        print(lines[1:7])
    if user_gender =="Girl" and user_number =="7":
        print(lines[1:8])
    if user_gender=="Girl" and user_number =="8":
        print(lines[1:9])
    if user_gender =="Girl" and user_number =="9":
        print(lines[1:10])
    if user_gender =="Girl" and user_number =="10":
        print(lines[1:11])
    elif user_gender =="Boy" and user_number =="1":
        print(lines[12])
    elif user_gender =="Boy" and user_number =="2":
        print(lines[12:14])
    elif user_gender =="Boy" and user_number =="3":
        print(lines[12:15])
    elif user_gender =="Boy" and user_number =="4":
        print(lines[12:16])
    elif user_gender =="Boy" and user_number =="5":
        print(lines[12:17])
    elif user_gender =="Boy" and user_number =="6":
        print(lines[12:18])
    elif user_gender =="Boy" and user_number =="7":
        print(lines[12:19])
    elif user_gender =="Boy" and user_number =="8":
        print(lines[12:20])
    elif user_gender =="Boy" and user_number =="9":
        print(lines[12:21])
    elif user_gender =="Boy" and user_number =="10":
        print(lines[12:22])
    elif user_gender =="Unisex" and user_number =="1":
        print(lines[23:24])
    elif user_gender =="Unisex" and user_number =="2":
        print(lines[23:25])
    elif user_gender =="Unisex" and user_number =="3":
        print(lines[23:26])
    elif user_gender =="Unisex" and user_number =="4":
        print(lines[23:27])
    elif user_gender =="Unisex" and user_number =="5":
        print(lines[23:28])
    elif user_gender =="Unisex" and user_number =="6":
        print(lines[23:29])
    elif user_gender =="Unisex" and user_number =="7":
        print(lines[23:30])
    elif user_gender =="Unisex" and user_number =="8":
        print(lines[23:31])
    elif user_gender =="Unisex" and user_number =="9":
        print(lines[23:32])
    elif user_gender =="Unisex" and user_number =="10":
        print(lines[23:33])

    


# label  and entry for gender

gender_label = tk.Label(text="Enter a gender from the following :", width=26,
                         height=2)
gender_label.grid(row=1, column=1, sticky="n")

gender_entry = tk.Entry(width=20)
gender_entry.grid(row=1, column=1, pady=10, sticky="s")

# setting status for user to see on gui 

status1 = tk.Label(text="Please enter a gender.....")
status1.grid(row=1, column =1, pady = 60, sticky ="n")


enter = "Please enter"
correct = "Correct!"
enter2 = "Please re-enter"

genders = ['Girl', 'Boy', 'Unisex']

# gender function to get gender from user 

def isGender():


    input1 = gender_entry.get()


    if len(input1) == 0:
        status1.configure(text=enter)
    elif input1 in genders:
        status1.configure(text=correct)
    else:
        status1.configure(text=enter2)
        
    return

user_gender = gender_entry.get()

status1.cget("text")

# entry and label for gender
gender_button = tk.Button(text="Enter", width=5, command = isGender)
gender_button.grid(row=1, column=1, pady=10, sticky="se")


gender_option = tk.Label(text="Boy, Girl, Unisex")
gender_option.grid(row=1, column=1, pady=30,sticky='n')



# label and entry for number

number_label = tk.Label(text="Enter a number between 1 - 10", width=25, 
                        height=2)
number_label.grid(row=2, column=1, sticky="n")

number_entry = tk.Entry(width=10)
number_entry.grid(row=2, column=1, pady=10, sticky="s")

# status for user on number function

status2 = tk.Label(text="Please enter a number....")
status2.grid(row=2, column=1, pady=50, sticky="n")

# function for getting number from user

def isNumber():

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    input2 = number_entry.get()

    if len(input2) == 0:
        status2.configure(text=enter)
    elif input2 in numbers:
        status2.configure(text=correct)
    else:
        status2.configure(text=enter2)

user_number = number_entry.get()

status2.cget("text")

number_button = tk.Button(text="Enter", width=5, command=isNumber)
number_button.grid(row=2, column=1, pady=10, sticky="se")


    
# final button for generating the names

generator_button = tk.Button(text="Generate Names", command= lambda: 
                             [print_name3(user_gender, user_number)], width=15,
                             height=5, bg="red",fg="white")
generator_button.grid(row=4, column=1, pady=20)

# help button for users

def help():
    tkinter.messagebox.showinfo("Information for error", 
                                "Please use the 'enter' button to validate your"
                                " input if unsure. The printed statment on the " 
                                "screen should show 'correct'. Remember the "
                                "gender should start with a capital letter and "
                                "the number should be written numerically.")


help_button = tk.Button(text="Why do I have no names?", command=help, height=2,
                         width=20, bg="lightgreen")
help_button.grid(row=0, column=2) 


window.mainloop()
