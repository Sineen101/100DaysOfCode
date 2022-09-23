from tkinter import *
import requests


def get_quote():
    # Get the response from the API endpoint
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()  # raise exception if status code is not 200
    quote = response.json()["quote"]  # Get the quote from the response
    canvas.itemconfig(quote_text, text=f'"{quote}"')


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=400)
background = PhotoImage(file="popup.png")
canvas.create_image(200, 207, image=background)
quote_text = canvas.create_text(
    200, 207, width=250, font=("Arial", 15, "bold"), fill="black")
canvas.grid(row=0, column=0)

name_img = PhotoImage(file="button.png")
button = Button(image=name_img, highlightthickness=0, command=get_quote)
button.grid(row=1, column=0)

window.mainloop()
