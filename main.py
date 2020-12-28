from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
cur_card = {}

# Random Data Generating
def generate_random():
    global cur_card, flip_timer
    window.after_cancel(flip_timer)
    cur_card = random.choice(dict)
    word = cur_card["French"]
    canvas.itemconfig(title_id, text="French", fill="black")
    canvas.itemconfig(word_id, text=word, fill="black")
    canvas.itemconfig(img_id, image=trg_img)
    flip_timer = window.after(3000, flip_card)


# Change Card Lang
def flip_card():
    en_word = cur_card["English"]
    canvas.itemconfig(img_id, image=b_img)
    canvas.itemconfig(title_id, text="English", fill="white")
    canvas.itemconfig(word_id, text=en_word, fill="white")


# Delete card
def delete_card():
    global data
    if cur_card in dict:
        dict.remove(cur_card)
        print(cur_card, "  ¡¡¡Eliminada!!!")
        data = data[data.French != cur_card["French"]]
        print(data)


# Data Reading
try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

print(data)
dict = data.to_dict("records")

# UI Setup
window = Tk()
window.title("Flash Cards Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=525, highlightthickness=0, bg=BACKGROUND_COLOR)
trg_img = PhotoImage(file="images/card_front.png")
b_img = PhotoImage(file="images/card_back.png")
img_id = canvas.create_image(410, 275, image=trg_img)
canvas.grid(column=0, row=0, columnspan=2)
title_id = canvas.create_text(410, 150, text="", font=FONT_LANG)
word_id = canvas.create_text(410, 275, text="", font=FONT_WORD)

wrong_image = PhotoImage(file="images/wrong.png")
w_button = Button(image=wrong_image, highlightthickness=0, command=generate_random)
w_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
r_button = Button(image=right_image, highlightthickness=0, command=delete_card)
r_button.grid(column=1, row=1)

generate_random()
window.mainloop()

data.to_csv("data/to_learn.csv", index=False)

