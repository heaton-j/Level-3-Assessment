import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

window = tk.Tk()

window.rowconfigure([0, 1, 2, 3, 4], minsize=150, weight=1)
window.columnconfigure([0, 1], minsize=250, weight=1)

# main title for generator
main_title = tk.Label(text="Baby Name Generator",
                      width=18, height=3, font=('Times', 18))
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


def get_gender():
    tk.Label.config(text=gender_entry.get())


gender_entry = tk.Entry(gender_frame, width=10)
gender_entry.grid(row=1, column=1)


# creating the pop up message for names
def onClick():
    tkinter.messagebox.showinfo("Names:")


# button for generating the names
generator_button = tk.Button(
    text="Generate Names", command=onClick, width=15, height=5, bg="red",
    fg="white")
generator_button.grid(row=4, column=0)

window.mainloop()