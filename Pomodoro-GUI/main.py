from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# -------------------------------Global Variables -------------------------- #
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    timer_lable.config(text="Timer", fg=GREEN)
    tickmark_label.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")
    global reps
    reps = 0
    button_start.config(state=NORMAL)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_min_secs = WORK_MIN*60
    short_break_Secs = SHORT_BREAK_MIN*60
    long_break_secs = LONG_BREAK_MIN*60
    button_start.config(state=DISABLED)

    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_lable.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_Secs)
        timer_lable.config(text="Short Break", fg=PINK)
    else:
        count_down(work_min_secs)
        timer_lable.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + f"{count_sec}"

    if count_min < 10:
        count_min = "0" + f"{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)

        for _ in range(work_sessions):
            marks += "✔"
        tickmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas Setup on Window
canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="D:/Python/python/Pomodoro-GUI/tomato.png")
canvas.create_image(100, 113, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Label = Timer
timer_lable = Label(text="Timer", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 35, "bold"))
timer_lable.grid(row=0, column=1)

# Label = Ticks (✔)
tickmark_label = Label(bg=YELLOW, fg=GREEN, font=(35))
tickmark_label.grid(row=3, column=1)

# Button 1 = Start
button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

# Button 2 = Reset
button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(row=2, column=2)

window.mainloop()
