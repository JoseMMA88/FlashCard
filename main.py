from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")


# Random Data Generating
def generate_random():
    rand_int = random.randint(0, len(dict) - 1)
    wo = dict[rand_int]["French"]
    canvas.itemconfig(word_id, text=wo)


# Data Reading
data = pandas.read_csv("data/french_words.csv")
dict = data.to_dict("records")
print(dict)


# UI Setup
window = Tk()
window.title("Flash Cards Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=525, highlightthickness=0, bg=BACKGROUND_COLOR)
trg_img = PhotoImage(file="images/card_front.png")
canvas.create_image(410, 275, image=trg_img)
canvas.grid(column=0, row=0, columnspan=2)
title_id = canvas.create_text(410, 150, text="French", font=FONT_LANG)
word_id = canvas.create_text(410, 275, text="word", font=FONT_WORD)

wrong_image = PhotoImage(file="images/wrong.png")
w_button = Button(image=wrong_image, highlightthickness=0, command=generate_random)
w_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
r_button = Button(image=right_image, highlightthickness=0, command=generate_random)
r_button.grid(column=1, row=1)

window.mainloop()

