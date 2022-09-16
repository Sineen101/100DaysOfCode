from playsound import playsound
from tkinter import *
import math

#--------------CONSTANTS--------------#
PINK = "#FF8080"
RED = "#C21010"
GREEN = "#CFE8A9"
YELLOW = "#FFFDE3"
FONT_NAME = "Helvatica"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None
#-----------------TIMER RESET-----------------#


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")

#-----------------TIMER MECHANISM-----------------#


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=YELLOW)
    else:
        countdown(work_sec)
        title_label.config(text="WORK", fg=GREEN)

    countdown(WORK_MIN * 60)


#-----------------COUNTDOWN MECHANISM-----------------#
def play():
    playsound("1.mp3")


def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # 1000ms = 1s; wait 1s and call countdown again
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)
        play()


#-----------------UI CODE BLOCK-----------------#
window = Tk()       # Create a window
window.title("Pomodoro Timer")  # Set title
window.config(padx=100, pady=50, bg=PINK)      # Set padding


title_label = Label(text="Timer", fg=GREEN, bg=PINK,
                    font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)    # Set title label


canvas = Canvas(width=220, height=220, bg=PINK,
                highlightthickness=0)       # Create a canvas
tomato_img = PhotoImage(file="tomato.png")  # Load an image
# Add an image to the canvas
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(99, 100, text="00:00",
                                fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)   # Set canvas grid


start_button = Button(text="Start", fg="white", bg=RED,
                      font=(FONT_NAME, 15), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)  # Set start button grid

reset_button = Button(text="Reset", fg="white", bg=RED,
                      font=(FONT_NAME, 15), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)  # Set reset button grid

check_marks = Label(fg=GREEN, bg=PINK, font=(FONT_NAME, 35, "bold"))
check_marks.grid(row=3, column=1)


window.mainloop()   # Create an event loop
