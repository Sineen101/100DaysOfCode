from tkinter import *
from pandas import *
from random import choice, shuffle, randint


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def known_card():
    to_learn.remove(current_card)
    DataFrame(to_learn).to_csv("words_to_learn.csv", index=False)

    next_card()


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=card_back)


to_learn = {}
current_card = {}

try:
    data = read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


window = Tk()
window.title("Flash Cards App")
window.config(padx=50, pady=50, bg="white")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=500, height=450, bg="white", highlightthickness=0)
card_front = PhotoImage(file="flash_card.png")
card_back = PhotoImage(file="flash_card_back.png")
card = canvas.create_image(250, 220, image=card_front)
title = canvas.create_text(250, 140, text="",
                           font=("Arial", 25, "italic"))
word = canvas.create_text(250, 260, text="", font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

img1 = PhotoImage(file="cross.png")
cross = Button(image=img1,
               highlightthickness=0, command=next_card)
cross.grid(row=1, column=0)

img2 = PhotoImage(file="check.png")
check = Button(image=img2,
               highlightthickness=0, command=known_card)
check.grid(row=1, column=1)

next_card()

window.mainloop()
