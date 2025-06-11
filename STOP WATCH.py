import tkinter as tk
from datetime import datetime
import time

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⏱ Stopwatch & Clock")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        # Clock Label
        self.clock_label = tk.Label(root, text="", font=("Arial", 18), fg="#333", bg="#f0f0f0")
        self.clock_label.pack(pady=10)
        self.update_clock()

        # Stopwatch Variables
        self.start_time = None
        self.running = False
        self.elapsed_time = 0

        # Stopwatch Label
        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Arial", 32), fg="#222", bg="#f0f0f0")
        self.stopwatch_label.pack(pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(btn_frame, text="Start", width=10, command=self.start)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop", width=10, command=self.stop)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(btn_frame, text="Reset", width=10, command=self.reset)
        self.reset_btn.grid(row=0, column=2, padx=5)

        # Run the stopwatch updater
        self.update_stopwatch()

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=f"🕒 Current Time: {now}")
        self.root.after(1000, self.update_clock)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")

    def update_stopwatch(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        minutes, seconds = divmod(int(self.elapsed_time), 60)
        hours, minutes = divmod(minutes, 60)
        self.stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        self.root.after(500, self.update_stopwatch)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchClockApp(root)
    root.mainloop()
