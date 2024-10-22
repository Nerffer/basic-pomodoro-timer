import tkinter as tk
from tkinter import messagebox

# creating the root window
root = tk.Tk()
root.title("Pomodoro Timer")
label = tk.Label(root, text="Pomodoro Timer", font=("Arial", 32))
label.pack(pady = 10)

# setting the window size
root.geometry("600x400")

# defining durations for the cycles, i will make them changeable with user inputs
work_duration = 25 * 60     # 25 minutes in seconds
break_duration = 5 * 60     # 5 minutes in seconds

# global variable to control time
time_remaining = work_duration
is_break = False
running = False

# setting the timer display
time_label = tk.Label(text="25:00", font=(None,50))
time_label.pack(pady = 50)

# implementing functions for the buttons
def update_timer():
    global time_remaining, is_break, running
    if running and time_remaining > 0:
        minutes, seconds = divmod(time_remaining, 60)
        time_label.config(text=f"{minutes:02}:{seconds:02}")
        time_remaining -= 1
        root.after(1000, update_timer)
    elif time_remaining == 0:
        if is_break:
            time_remaining = work_duration
            is_break = False
            time_label.config(text="25:00")
            label.config(text="Pomodoro Timer")
            messagebox.showinfo("Pomodoro Timer", "Break time ended! Back to work.")
        else:
            time_remaining = break_duration
            is_break = True
            time_label.config(text="05:00")
            label.config(text="Break Time!")
            messagebox.showinfo("Pomodoro Timer", "Work session ended! Time to take a break.")
        running = False
# start function
def start_timer():
    global running
    if not running:
        running = True
        update_timer()
# stop function
def stop_timer():
    global running
    running = False
# reset function
def reset_timer():
    global time_remaining, running, is_break
    running = False
    is_break = False
    time_remaining = work_duration
    time_label.config(text="25:00")
    label.config(text="Pomodoro Timer")

# implementing the buttons
start = tk.Button(root, text="Start", width=10, height=2, font=(None, 16), command=start_timer)
start.pack(side="left", padx=5, expand=True)
stop = tk.Button(root, text="Stop", width=10, height=2, font=(None, 16), command=stop_timer)
stop.pack(side="left", padx=5, expand=True)
reset = tk.Button(root, text="Reset", width=10, height=2, font=(None, 16), command=reset_timer)
reset.pack(side="left", padx=5, expand=True)
# run the main loop
root.mainloop()