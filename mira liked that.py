import tkinter as tk
from PIL import ImageColor
import pygame
import os
import sys
import time

# Function to convert hex to RGB
def hex_to_rgb(hex_color):
    return ImageColor.getcolor(hex_color, "RGB")

# Function to initialize Pygame and play audio
def initialize_audio(audio_file):
    pygame.mixer.init()
    if not os.path.exists(audio_file):
        print(f"Error: The file {audio_file} does not exist.")
        sys.exit(1)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(-1)

# Function to create a "not responding" window
def not_responding_window():
    global root, canvas, label, terminal

    root = tk.Tk()
    root.attributes("-fullscreen", True)

    hex_color = "#008B8B"
    rgb_color = hex_to_rgb(hex_color)
    root.configure(bg=f"#{rgb_color[0]:02x}{rgb_color[1]:02x}{rgb_color[2]:02x}")

    canvas = tk.Canvas(root, bg=f"#{rgb_color[0]:02x}{rgb_color[1]:02x}{rgb_color[2]:02x}", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    button_width = 100
    button_height = 50
    canvas_width = root.winfo_screenwidth()
    canvas_height = root.winfo_screenheight()
    button_coords = [
        (canvas_width // 2 - button_width // 2, canvas_height // 2 - button_height // 2),
        (canvas_width // 2 + button_width // 2, canvas_height // 2 - button_height // 2),
        (canvas_width // 2 + button_width // 2, canvas_height // 2 + button_height // 2),
        (canvas_width // 2 - button_width // 2, canvas_height // 2 + button_height // 2),
    ]

    button = canvas.create_polygon(button_coords, fill="white", outline="black")
    text_x = canvas_width // 2
    text_y = canvas_height // 2
    text = canvas.create_text(text_x, text_y, text="hello", font=("Arial", 20))

    label = tk.Label(root, text="", font=("Arial", 40), bg=f"#{rgb_color[0]:02x}{rgb_color[1]:02x}{rgb_color[2]:02x}", fg="white")
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    terminal = tk.Text(root, height=10, width=40, bg="black", fg="green", font=("Courier", 12), highlightthickness=0)
    terminal.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    terminal.insert(tk.END, "Initializing terminal...\n")
    terminal.config(state=tk.DISABLED)

    def trigger_not_responding(event=None):
        if not trigger_not_responding.has_triggered:
            label.config(text="not responding")
            trigger_not_responding.has_triggered = True
            start_krate()

    trigger_not_responding.has_triggered = False

    canvas.bind("<Motion>", lambda event: event)
    canvas.tag_bind(button, "<Enter>", trigger_not_responding)
    canvas.tag_bind(text, "<Enter>", trigger_not_responding)

    root.after(60000, deadlained)  # Call deadlained function after 1 minute
    root.mainloop()

# Function to simulate the terminal countdown
def start_krate():
    terminal.config(state=tk.NORMAL)
    for i in range(60, 0, -1):
        terminal.insert(tk.END, f"Krate: {i} seconds remaining\n")
        terminal.see(tk.END)
        terminal.update()
        time.sleep(1)
    terminal.config(state=tk.DISABLED)

# Function to switch to the "not responding" window
def switch_to_not_responding():
    root.destroy()
    not_responding_window()

# Function to switch to the simple window
def switch_to_krate():
    root.destroy()
    simple_window()

# Reset protocol for the "not responding" window
def deadlained():
    root.destroy()
    not_responding_window()

# Initialize the audio and start with the "not responding" window
audio_file = "samplegalaxyambientmenu(2).wav"
initialize_audio(audio_file)
not_responding_window()
