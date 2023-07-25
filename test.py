import tkinter as tk
app = tk.Tk()
app.geometry("300x100")
def switchButtonState():
    if (button1['state'] == tk.NORMAL):
        button1['state'] = tk.DISABLED
    else:
        button1['state'] = tk.NORMAL
button1 = tk.Button(app, text="Python Button 1",
                    state=tk.DISABLED)
button2 = tk.Button(app, text="EN/DISABLE Button 1",
                    command = switchButtonState)
button1.pack(side=tk.LEFT)
button2.pack(side=tk.RIGHT)

app.mainloop()