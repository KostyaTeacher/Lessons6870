import tkinter as tk
from tkinter import messagebox

def start_clicker():
    # тут буде запуск клікера
    messagebox.showinfo("Auto Clicker", "Auto Clicker запушено. Натисни 'ESC' щоб зупинити.")


def exit_app():
    # тут буде завершення програми
    root.destroy() # Close the Tkinter window


root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x220")
root.configure(bg="#e0f7fa") # Light blue background

# Label: назва
title_label = tk.Label(root, text="Auto Clicker", font=("Trebuchet MS", 16, "bold"), bg="#e0f7fa", fg="#00796b")
title_label.pack(pady=10) # Add some padding

# Label: кліки на секунду
label = tk.Label(root, text="Кліків на секунду:", font=("Trebuchet MS", 12), bg="#e0f7fa", fg="#00796b")
label.pack(pady=5)

# Entry для кількості кліків
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Frame, в якому будуть кнопки "почати" і "вийти"
button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(20, 30)) # Increase padding from the bottom

# Кнопка "Почати"
start_button = tk.Button(button_frame, text="Почати", command=start_clicker, bg="#4caf50", fg="white", font=("Trebuchet MS", 12))
start_button.grid(row=0, column=0, padx=10) # Add horizontal padding

# Кнопка "Вийти"
exit_button = tk.Button(button_frame, text="Вийти", command=exit_app, bg="#f44336", fg="white", font=("Trebuchet MS", 12))
exit_button.grid(row=0, column=1, padx=10) # Add horizontal padding


root.mainloop()