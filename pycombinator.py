import tkinter as tk
from turtle import width

# Setup the application window
window = tk.Tk()
window.geometry("800x600")
window.title("PyCombinator")
window.resizable(0,0)

# Configure the grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Welcome
welcome_label = tk.Label(window, text="Pycombinator by jwinterm @ Laumalex Software - copyright 2022")
welcome_label.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

# Directory
dir_label = tk.Label(window, text="Images directory:")
dir_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
dir_entry = tk.Entry(window, width=70)
dir_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# Run the main application loop
window.mainloop()