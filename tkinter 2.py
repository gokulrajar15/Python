
import tkinter as tk
win = tk.Tk()
win.geometry("300x300")
top_button = tk.Button(win, text="Top")
bottom_button = tk.Button(win, text="Bottom")
left_button = tk.Button(win, text="Left", fg='black')
right_button = tk.Button(win, text="Right")
top_button.pack(side="top")
bottom_button.pack(side="bottom")
left_button.pack(side="left")
right_button.pack(side="right")
win.mainloop()
