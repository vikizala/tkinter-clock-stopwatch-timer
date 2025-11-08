import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

i = time.time()
p = time.localtime(i)
g = time.strftime("%H:%M:%S", p)
h = time.strftime("%d:%m:%Y", p)

class CountdownTimer:
    def __init__(self, root):  # Corrected constructor name
        self.root = root
        self.root.title("Countdown Timer")

        tabs = ttk.Notebook(root)
        clock_tab = tk.Frame(tabs)
        stop_tab = tk.Frame(tabs)
        timer_tab = tk.Frame(tabs)

        tabs.add(clock_tab, text="часы")
        tabs.add(stop_tab, text="секундомер")
        tabs.add(timer_tab, text="тайме")
        tabs.pack(expand=1, fill=tk.BOTH)

        # Time variables
        self.hour = tk.StringVar(value='00')
        self.minute = tk.StringVar(value='00')
        self.second = tk.StringVar(value='00')

        # Create entry widgets
        self.hourEntry = tk.Entry(root, width=3, font=("Arial", 18, ""), textvariable=self.hour)
        self.hourEntry.place(x=80, y=30)

        tk.Label(root, text=":", font=("Arial", 18)).place(x=120, y=30)

        self.minuteEntry = tk.Entry(root, width=3, font=("Arial", 18, ""), textvariable=self.minute)
        self.minuteEntry.place(x=140, y=30)

        tk.Label(root, text=":", font=("Arial", 18)).place(x=180, y=30)

        self.secondEntry = tk.Entry(root, width=3, font=("Arial", 18, ""), textvariable=self.second)
        self.secondEntry.place(x=200, y=30)

        # Buttons
        self.begin = tk.Button(timer_tab, text="Start", bd=5, command=self.start_timer)
        self.begin.place(x=80, y=100)

        self.stop = tk.Button(timer_tab, text="Stop", bd=5, command=self.stop_timer)
        self.stop.place(x=140, y=100)

        self.reset = tk.Button(timer_tab, text="Reset", bd=5, command=self.reset_timer)
        self.reset.place(x=200, y=100)

        self.begin = tk.Button(stop_tab, text="Start", bd=5, command=self.start_timer_2)
        self.begin.place(x=80, y=100)

        self.stop = tk.Button(stop_tab, text="Stop", bd=5, command=self.stop_timer)
        self.stop.place(x=140, y=100)

        self.reset = tk.Button(stop_tab, text="Reset", bd=5, command=self.reset_timer)
        self.reset.place(x=200, y=100)

        self.reset = tk.Button(clock_tab, text=(f"{g}, {h}"), bd=5, command=self.reset_timer)
        self.reset.place(x=100, y=100)

        self.is_running = False
        self.remaining_seconds = 0


    def start_timer(self):
        if not self.is_running:
            try:
                hours = int(self.hour.get())
                minutes = int(self.minute.get())
                seconds = int(self.second.get())

                if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
                    raise ValueError("Invalid time values")

                self.remaining_seconds = hours * 3600 + minutes * 60 + seconds

                if self.remaining_seconds > 0:
                    self.is_running = True
                    self.update_timer()

            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers for time (HH:MM:SS)")

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.hour.set('00')
        self.minute.set('00')
        self.second.set('00')

    def update_timer(self):
        if self.is_running and self.remaining_seconds > 0:
            hours, remainder = divmod(self.remaining_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            self.hour.set(str(hours).zfill(2))
            self.minute.set(str(minutes).zfill(2))
            self.second.set(str(seconds).zfill(2))

            self.remaining_seconds -= 1
            self.root.after(1000, self.update_timer)
        elif self.remaining_seconds == 0 and self.is_running:
            self.is_running = False
            messagebox.showinfo("Timer", "Time's up!")
            self.reset_timer()

    def start_timer_2(self):

        try:
            hours = 0
            minutes = 0
            seconds = 0
            if hours < 0 or minutes < 0 or seconds < 0 or minutes >= 60 or seconds >= 60:
                raise ValueError("Invalid time values")

            self.remaining_seconds = hours * 3600 + minutes * 60 + seconds

            if self.remaining_seconds >= 0:
                self.is_running = True
                self.update_timer_2()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for time (HH:MM:SS)")

    def update_timer_2(self):
        if self.is_running and self.remaining_seconds >= 0:
            hours, remainder = divmod(self.remaining_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            self.hour.set(str(hours).zfill(2))
            self.minute.set(str(minutes).zfill(2))
            self.second.set(str(seconds).zfill(2))

            self.remaining_seconds += 1
            self.root.after(1000, self.update_timer_2)
        elif self.remaining_seconds != 0 and self.is_running:
            self.is_running = False
            messagebox.showinfo("Timer", "Time's up!")
            self.reset_timer()



if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.geometry("300x200")
    root.mainloop()