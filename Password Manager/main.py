import email
from re import search
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


#------------------SAVE PASSWORD------------------#
def save_password():
    global e1, e2, e3
    website = e1.get()
    email = e2.get()
    passwd = e3.get()
    new_data = {
        website: {
            "email": email,
            "password": passwd,
        }
    }

    if len(website) == 0 or len(passwd) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as f:
                # Reading old data in the file to a dictionary
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                # This will overwrite the data in the file
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)  # Updating the old data with the new data
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e1.focus()


#------------------GENERATE PASSWORD------------------#


def passwd_generator():
    global e3
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
               '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ':', ';', '"', '<', '>', '?', '.', '/', '~', '`', ' ']
    password = [choice(letters) for _ in range(randint(8, 10))]
    password += [choice(symbols) for _ in range(randint(2, 5))]
    password += [choice(numbers) for _ in range(randint(2, 5))]
    shuffle(password)             # Shuffles the password

    passwd = "".join(password)            # Converts the password to a string
    e3.insert(0, passwd)
    pyperclip.copy(passwd)


#------------------SEARCH PASSWORD------------------#
def search_password():
    website = e1.get()
    try:
        with open("data.json") as f:
            data = json.load(f)  # Reading the data from the file
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="No Data Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists.")


# -----------------UI CODE BLOCK-----------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
window.minsize(width=500, height=500)

# -----------------CANVAS CODE BLOCK-----------------#
canvas = Canvas(width=200, height=200,
                bg="white", highlightthickness=0)
logo = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# -----------------LABEL CODE BLOCK-----------------#
l1 = Label(text="Website:", bg="white")
l2 = Label(text="Email/Username:", bg="white")
l3 = Label(text="Password:", bg="white")
l1.grid(row=1, column=0)
l1.focus()
l2.grid(row=2, column=0)
l3.grid(row=3, column=0)

# -----------------ENTRY CODE BLOCK-----------------#
e1 = Entry(width=21)
e2 = Entry(width=43)
e3 = Entry(width=21)
e1.grid(row=1, column=1, columnspan=1)
e2.grid(row=2, column=1, columnspan=2)
e2.insert(0, "random@gmail.com")
e3.grid(row=3, column=1, columnspan=1)

# -----------------BUTTON CODE BLOCK-----------------#
b0 = Button(width=14, text="Search", bg="#80b3ff", command=search_password)
b1 = Button(text="Generate Password", bg="#80b3ff", command=passwd_generator)
b2 = Button(width=61, text="Add", bg="#80b3ff", command=save_password)
b0.grid(row=1, column=2, padx=5, pady=5)
b1.grid(row=3, column=2)
b2.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
