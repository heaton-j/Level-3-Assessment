import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

window = tk.Tk()

window.rowconfigure([0, 1, 2, 3, 4], minsize=150, weight=1)
window.columnconfigure([0, 1], minsize=250, weight=1)

# main title for generator
main_title = tk.Label(text="Baby Name Generator",
                      width=18, height=6, font=('Times', 8))
main_title.grid(row=0, column=0)


# background frame for gender option
gender_frame = tk.Frame(master=window, bg="lightgreen")
gender_frame.grid(row=1, column=1, sticky="nsew")


# background frame for style option
style_frame = tk.Frame(master=window, bg="lightblue")
style_frame.grid(row=2, column=1, sticky="nsew")

# background frame for number option
number_frame = tk.Frame(master=window, bg="lightpink")
number_frame.grid(row=3, column=1, sticky="nsew")


# label for gender
gender_label = tk.Label(text="Enter a gender from the following :", width=26,
                        height=2, font=('Times', 13))
gender_label.grid(row=1, column=1, sticky="n")

# labels for gender options
gender_option = tk.Label(text="Male, Female, Gender Neutral")
gender_option.grid(row=1, column=1)

# entry for gender
gender_entry = tk.Entry(width=10)
gender_entry.grid(row=1, column=1, pady=10, sticky="s")

# entry button for gender
gender_button = tk.Button(width=5)
gender_button.grid(row=1, column=1, padx=10, sticky="se")

gender_list = ["Female", "Male", "Gender Neutral"]


def gender():
    gender_entry = ""
    if gender_entry in gender_list:
        print("The gender you chose is {}".format(gender_entry))
    else:
        print("Please re-enter a gender value from the 3 options available")


# label for style
style_label = tk.Label(text="Enter a style", width=12, height=2,
                       font=('Times', 8))
style_label.grid(row=2, column=1, sticky="n")


# label for number
number_label = tk.Label(text="Enter a number between 1 - 5", width=25,
                        height=2, font=('Times', 8))
number_label.grid(row=3, column=1, sticky="n")


# creating the pop up message for names


def onClick():
    tkinter.messagebox.showinfo("Names:")


# button for generating the names
generator_button = tk.Button(
    text="Generate Names", command=onClick, width=15, height=5, bg="red",
    fg="white")
generator_button.grid(row=4, column=1)

window.mainloop()
