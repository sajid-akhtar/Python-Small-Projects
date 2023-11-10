from tkinter import *
import requests


# --------------------------- Get Quotes - Function ---------------------------------------- #

def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    value = response.json()["quote"]
    canvas.itemconfig(quote_text, text=value)

# ------------------------------ Window Configuration --------------------------------- #


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# ----------------------------- Canvas Configuration ------------------------------------- #

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(
    file="D:/Python/python/Kanye-Quotes-Gui-App/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=(
    "Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)
get_quote()

kanye_img = PhotoImage(file="D:/Python/python/Kanye-Quotes-Gui-App/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
