import tkinter as tk

root = tk.Tk()

# Отримуємо розміри екрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Розраховуємо нові розміри вікна
new_width = screen_width // 2 # Половина ширини екрану
new_height = screen_height # Вся висота екрану

size = f"{new_width}x{new_height}"
size_screen = f"Ваш монітор має розмір: {screen_width }x{screen_height}"
# Задаємо нові розміри вікна
root.geometry(size)

title_label = tk.Label(root, text=size_screen, font=("Trebuchet MS", 16, "bold"), bg="#e0f7fa", fg="#00796b")
title_label.pack(pady=10) # Add some padding



root.mainloop()