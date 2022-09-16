from tkinter import *


def action():
    """This function converts the weight from kilograms to pounds."""
    weight_in_kg = float(
        input.get())   # This is how we get the value from the entry widget.
    weight_in_lbs = weight_in_kg * 2.20462  # This is the conversion formula.
    # This is how we change the text of the label widget.
    label4.config(text=str(round(weight_in_lbs, 2)))


# window
window = Tk()  # Creates a window.
window.title("Weight Converter")  # This is the title of the window.
# This is the minimum size of the window.
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)  # This is the padding of the window.

# Labels
label1 = Label(text="Kg")  # This is the label for the entry widget.
label2 = Label(text="equals to")
label3 = Label(text="Pounds")
label4 = Label(text="0")
label1.grid(column=2, row=0)
label2.grid(column=0, row=1)
label3.grid(column=2, row=1)
label4.grid(column=1, row=1)

# input
input = Entry(width=10)  # This is the entry widget.
input.insert(END, string="0")  # This is the default value of the entry widget.
input.grid(column=1, row=0)  # This is how we position the entry widget.

# button
button = Button(text="Calculate", command=action)  # This is the button widget.
button.grid(column=1, row=2)

window.mainloop()   # Keep the window open
