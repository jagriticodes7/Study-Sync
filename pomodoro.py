import tkinter as tk
from tkinter import messagebox
# creating main window
root = tk.Tk()
root.title("StudySync Café")
root.geometry("900x650")
root.configure(bg="#F3F0E9")
root.resizable(True, True)
# Creating screen containers
welcome_frame = tk.Frame(root, bg="#F3F0E9")
drink_frame = tk.Frame(root, bg="#F3F0E9")
duration_frame = tk.Frame(root, bg="#F3F0E9")
intention_frame = tk.Frame(root, bg="#F3F0E9")
timer_frame = tk.Frame(root, bg="#F3F0E9")

# Screen switching function
def show_screen(screen):
    welcome_frame.pack_forget()
    drink_frame.pack_forget()
    duration_frame.pack_forget()
    intention_frame.pack_forget()
    timer_frame.pack_forget()

    screen.pack(fill="both", expand=True)

# Welcome screen
welcome_title = tk.Label(
    welcome_frame,
    text="Welcome to StudySync Café ☕",
    font=("Georgia", 28),
    bg="#F3F0E9",
    fg="#29251F"
)

welcome_title.pack(pady=100)

welcome_subtitle = tk.Label(
    welcome_frame,
    text="Your little corner of focus and calm.",
    font=("Georgia", 16),
    bg="#F3F0E9"
)

welcome_subtitle.pack(pady=10)

enter_button = tk.Button(
    welcome_frame,
    text="Enter Café",
    font=("Georgia", 15),
    bg="#29251F",
    fg="white",
    command=lambda: show_screen(drink_frame)
)

enter_button.pack(pady=30)


# Display welcome screen
show_screen(welcome_frame)

# Run application
root.mainloop()
