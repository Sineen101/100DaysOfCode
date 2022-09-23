import smtplib
import datetime
import pandas
from tkinter import *


def info():
    global sender, passwd, smtp_server
    sender = sender_email.get()
    passwd = sender_password.get()
    smtp_server = ""
    if "@gmail" in sender:
        smtp_server = "smtp.gmail.com"
    elif "@yahoo" in sender:
        smtp_server = "smtp.mail.yahoo.com"
    elif "@hotmail" in sender:
        smtp_server = "smtp.live.com"
    elif "@icloud" in sender:
        smtp_server = "smtp.mail.me.com"
    elif "@protonmail" in sender:
        smtp_server = "smtp.protonmail.com"
    else:
        print("Email provider not supported")
    window.destroy()


now = datetime.datetime.now()
today = (now.month, now.day)
birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (
    index, row) in birthdays.iterrows()}

if today in birthdays_dict:
    name = birthdays_dict[today]["name"]
    email = birthdays_dict[today]["email"]
    with open("letter.txt") as q:
        qoute = q.read()
        content = qoute.replace("[name]", name)

window = Tk()
window.title("Custom Email Sender Login")
window.config(padx=20, pady=20, bg="black")
label1 = Label(text="Sender Email:", bg="black", fg="white")
label2 = Label(text="Password:", bg="black", fg="white")
label1.grid(column=0, row=0)
label2.grid(column=0, row=1)
sender_email = Entry(width=30)
sender_password = Entry(width=30)
sender_email.grid(column=1, row=0)
sender_password.grid(column=1, row=1)
button = Button(text="Send Email", bg="black", fg="white", command=info)
button.grid(column=1, row=2)
window.mainloop()

with smtplib.SMTP(smtp_server) as connection:
    # Secure the connection. TLS(Transport Layer Security) is a cryptographic protocol that provides communication security over the Internet.
    connection.ehlo()   # Identifies the client to the server.
    connection.starttls()
    connection.ehlo()   # Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email.
    # Login to the email account
    connection.login(user=sender, password=passwd)
    connection.sendmail(from_addr=sender, to_addrs=email,
                        msg=f"Subject:Happy Birthday!\n\n{content}")  # Send the email
