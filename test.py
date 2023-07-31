
def button():
    if "text" in status1 != correct:
        generator_button.config(state='normal')
    elif "text" in status3 != correct:
        generator_button.config(state='normal')
    else:
        generator_button.config(state='disbaled')

