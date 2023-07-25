import tkinter as tk
from tkinter import ttk
import tkinter.messagebox



window = tk.Tk()

window.rowconfigure([0, 1, 2, 3], minsize=130, weight=1)
window.columnconfigure([0, 1, 2], minsize=200, weight=1)

# main title for generator
main_title = tk.Label(text="Adult & Baby Name Generator",
                      width=18, height=6, font=('Times', 20))
main_title.grid(row=0, column=1)


# background frame for gender option
gender_frame = tk.Frame(master=window, bg="lightblue")
gender_frame.grid(row=1, column=1, sticky="nsew")


# background frame for number option
number_frame = tk.Frame(master=window, bg="lightpink")
number_frame.grid(row=2, column=1, sticky="nsew")


# label for gender
gender_label = tk.Label(text="Enter a gender  :", width=26,
                        height=2)
gender_label.grid(row=1, column=1, sticky="n")

# entry for gender
gender_entry = tk.Entry(width=10)
gender_entry.grid(row=1, column=1, pady=10, sticky="s")


status1 = tk.Label(text="Please enter a gender.....")
status1.grid(row=1, column =1, pady = 60, sticky ="n")


def isGender():


    genders = ['Female', 'Male', 'Gender Neutral']
    input1 = gender_entry.get()


    if len(input1) == 0:
        status1.configure(text="Please enter")
    elif input1 in genders:
        status1.configure(text="correct")
    else:
        status1.configure(text="Please re enter")


# entry button for gender
gender_button = tk.Button(text="Enter", width=5, command = isGender)
gender_button.grid(row=1, column=1, pady=10, sticky="se")


# labels for gender options
gender_option = tk.Label(text="Male, Female, Gender Neutral")
gender_option.grid(row=1, column=1, pady=30,sticky='n')

# creating the pop up message for names


def onClick():
    tkinter.messagebox.showinfo("Names:") 




# label for number
number_label = tk.Label(text="Enter a number between 1 - 5", width=25,
                        height=2)
number_label.grid(row=2, column=1, sticky="n")

number_entry = tk.Entry(width=10)
number_entry.grid(row=2, column=1, pady=10, sticky="s")

status3 = tk.Label(text="Please enter a number....")
status3.grid(row=2, column=1, pady=50, sticky="n")


def isNumber():

    numbers = ['1', '2', '3', '4', '5', [6]]
    input3 = number_entry.get()

    if len(input3) == 0:
        status3.configure(text="Please enter")
    elif input3 in numbers:
        status3.configure(text="Correct")
    else:
        status3.configure(text="Re-enter Value")


number_button = tk.Button(text="Enter", width=5, command=isNumber)
number_button.grid(row=2, column=1, pady=10, sticky="se")

# user check if both status are correct
Check_title = tk.Label(text="Have you correctly filled out all fields?")
Check_title.grid(row=3, column=1, pady=20)

yes = tk.Checkbutton(text="Yes", width=5)
yes.grid(row=3, column=1, pady=30, )

no = tk.Checkbutton(text="No", width=5)
no.grid(row=3, column=1, pady=40)


# button for generating the names
generator_button = tk.Button(
    text="Generate Names", command=onClick, width=15, height=5, bg="red",
    fg="white")
generator_button.grid(row=4, column=1)

generator_button.wait_variable

myfile = open("G:\My Drive\Digital Science\Level-3-Assessment/Names.txt","r")
for line in myfile:
    if line.startswith("Girl"):
        print(line)


myfile.readlines()


window.mainloop()
