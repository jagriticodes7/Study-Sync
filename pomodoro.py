import tkinter as tk

# Main window
root = tk.Tk()
root.title("StudySync Cafe")
root.geometry("800x600")
root.configure(bg="#F3F0E9")

# Heading
title = tk.Label(
    root,
    text="Welcome to StudySync Cafe!",
    font=("Arial", 24, "bold"),
    bg="#F3F0E9",
    fg="#594A42"
)
title.pack(pady=100)

# Subtitle
subtitle = tk.Label(
    root,
    text="Your little corner of focus and calm.",
    font=("Arial", 14),
    bg="#F3F0E9"
)
subtitle.pack(pady=10)

# Button function
def enter_cafe():
    title.config(text="Welcome inside! ☕")
    subtitle.config(text="Let's make today productive.")

# Enter button
button = tk.Button(
    root,
    text="Enter Cafe",
    font=("Arial", 14),
    command=enter_cafe
)
button.pack(pady=30)

# Keep window open
root.mainloop()
