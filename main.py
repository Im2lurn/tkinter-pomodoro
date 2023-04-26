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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    reps = 0
    title_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1

    if reps % 2 == 1:
        title_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)
    elif reps == 2 or 4 or 6:
        title_label.config(text="SHORT BREAK", fg=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        reps = 0
        title_label.config(text="LONG BREAK", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60

    if count_minute < 10:
        count_minute = f"0{count_minute}"
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        text1 = ""
        for index in range(math.floor(reps / 2)):
            text1 += "🍅"
        check_mark.config(text=text1)

        # to make a sound to indicate end of a session
        # works even if the window has been minimised
        window.bell()
        # to make the window jump to the front
        # only works if the window has not been minimised
        window.deiconify()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(bg=YELLOW, width=200, height=224, highlightthickness=0)
bg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=2)
button2 = Button(text="Reset", command=reset_timer)
button2.grid(column=3, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=2)
window.mainloop()
