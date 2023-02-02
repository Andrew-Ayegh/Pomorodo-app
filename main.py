from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """Reseting the applicatio interface to it's original state"""
    global rep
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    rep = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def stat_timer():
    """Starts the pomodoro timer"""
    global rep 
    rep += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if rep % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "Long-Break", foreground=YELLOW)
    elif rep % 2 == 0:
        timer_label.config(text = "Short-Break", foreground=RED)
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        timer_label.config(text="Work-Timer", foreground="Green")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """countdown mechanism """
    count_min = floor(count/60)
    count_sec = count % 60
    
    if count_sec == 0:
        count_sec = "00"
    elif count_sec <10 and count_sec>0:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text =f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
        
    else:
        stat_timer()
        marks = ""
        work_session = rep//2
        for _ in range(work_session):
            marks +="✔️"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
# Creating the display wnidow
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=PINK)




# Creating a timer label for the poomdoro windows
timer_label = Label(text="Timer", background=PINK, foreground=YELLOW, font=('harrington', 40))
timer_label.grid(row=0, column=1)

# Creating a canvas widget to lay elements ontop of each other
"""hightlightthickness manipulates the thickness of the canvas highlight layout"""
canvas = Canvas(width=200, height=224, background=PINK, highlightthickness=0)

# Reading through files to read an image which will the be usabel by tkinter's canvas widget
tomato_image = PhotoImage(file="tomato.png")

# creating image with canvas
canvas.create_image(100, 112, image=tomato_image)

# Creating text in the canvas
timer_text = canvas.create_text(100, 130,text="00:00", fill="black", font=("colonna MT", 40))
canvas.grid(row=1, column=1)

# Creating the start button
start_button = Button(text="Start", foreground="White", background=PINK, command=stat_timer)
start_button.grid(row=2, column=0)

# Creating reset button 
reset_button = Button(text="Reset", foreground="White", background=PINK, command=reset_timer)
reset_button.grid(row=2, column=2)

# Creating checkamarks
check_marks = Label(foreground="green", background=PINK)
check_marks.grid(column =1 , row= 3)




window.mainloop()