from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# --------------------------------------- Read Data From CSV File ------------------------------ #

try:
    data = pandas.read_csv(
        "D:/Python/python/Flash-Card-Gui-App/data/to_learn_from.csv")
except FileNotFoundError:
    data = pandas.read_csv(
        "D:/Python/python/Flash-Card-Gui-App/data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")


# ----------------------------------------- Function - Next Card -------------------------------- #


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=canvas_image_back)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(5000, func=flip_card)


# ----------------------------------------- Function - Flip Card -------------------------------- #


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=canvas_image_back)


# ----------------------------------------- Function - Is Known -------------------------------- #


def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(
        "D:/Python/python/Flash-Card-Gui-App/data/to_learn_from.csv", index=False)
    next_card()


# --------------------------------------- Window ----------------------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, func=flip_card)

# ----------------------------------------- Canvas ---------------------------------------------- #

canvas = Canvas(width=800, height=526)
canvas_image_front = PhotoImage(
    file="D:/Python/python/Flash-Card-Gui-App/images/card_front.png")
canvas_image_back = PhotoImage(
    file="D:/Python/python/Flash-Card-Gui-App/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=canvas_image_front)
card_title = canvas.create_text(
    400, 150, text="", font=("Aerial", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="", font=("Aerial", 60, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# ----------------------------------------------- Buttons ---------------------------------------- #

wrong_image = PhotoImage(
    file="D:/Python/python/Flash-Card-Gui-App/images/wrong.png")
right_image = PhotoImage(
    file="D:/Python/python/Flash-Card-Gui-App/images/right.png")
# Button 1
wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong.grid(row=1, column=0)

# Button 2
right = Button(image=right_image, highlightthickness=0, command=is_known)
right.grid(row=1, column=1)

# Initial Function call
next_card()

window.mainloop()
