from tkinter import *
import math
# ------------  Constants   -----------------

PINK = "#e2979c"
RED = "#ff0000"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 15
REPS = 0
timer = None

# ------------  TImer Reset  ----------------
def reset_timer():
     window.after_cancel(timer)
     timer_text.config(text="Timer", foreground=GREEN)
     checked["text"] = ""
     canvas.itemconfig(canvas_text, text="00:00")
     global REPS
     REPS = 0
# ------------  Timer Mechanism   -----------
def start_timer():
    global REPS
    REPS +=1
    if REPS % 8 == 0:
        timer_text.config(text="Long Break", foreground=RED)
        count_down(10)
    elif REPS % 2 == 0:
        timer_text.config(text="Break", foreground=PINK)
        count_down(5)
    else:
        timer_text.config(text="Work", foreground=GREEN)
        count_down(2)


# ------------  CountDown Mechanism   -------
def count_down(count):
    remaining_min = math.floor(count / 60)
    remaining_sec = count % 60
    if remaining_sec < 10:
        remaining_sec = f"0{remaining_sec}"
    canvas.itemconfig(canvas_text, text=f"{remaining_min}:{remaining_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            marks += "✔"
        checked["text"] = marks

# ------------  UI Setup    -----------------
window = Tk()
window.title("Pomodoro")
window.config(padx=25, pady=100, bg=YELLOW)

canvas = Canvas(width=640, height=356, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(320, 178, image=img)
canvas_text = canvas.create_text(320, 230, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=3)

timer_text = Label(text="Timer", font=(FONT_NAME, 40, "bold"), foreground=GREEN, bg=YELLOW)
timer_text.grid(row=1, column=3)

start = Button(text="Start", font=(FONT_NAME, 15, "normal"),command=start_timer)
start.grid(row=3, column=2)

reset = Button(text="Reset", font=(FONT_NAME, 15, "normal"), command=reset_timer)
reset.grid(row=3, column=4)

checked = Label(text="", font=(FONT_NAME, 12, "normal"))
checked.grid(row=4, column=3)
window.mainloop()
