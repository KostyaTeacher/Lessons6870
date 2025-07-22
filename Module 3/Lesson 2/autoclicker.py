import time
import tkinter as tk
from tkinter import messagebox
import keyboard
import mouse


running = False  # змінна, що зберігатиме стан: програма зараз працює або ні
delay = 0  # змінна, що зберігатиме тривалість перерви після кожного кліку


def start_clicker():
    global running, delay  # "знаходимо" змінні, що існують поза функцією
    clicks_per_second = int(entry.get())
    delay = 1 / clicks_per_second  # рахуємо затримку між кліками
    messagebox.showinfo("Auto Clicker", "Auto Clicker розпочинає роботу.")
    running = True
    # Запуск процесу кліків
    schedule_click()


def schedule_click():
    #sum = 0
    while running:
        mouse.click()
        # print(f"Ви клікнули {sum} разів")
        # sum += 1
    time.sleep(delay)  # затримка між кліками


def exit_app():
    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
    #root.destroy() # Закриття вікна Tkinter


def show_info(event):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

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
entry = tk.Entry(root, font=("Arial", 12), bd=0, highlightthickness=0, relief="flat")
entry.pack(pady=5)

# Frame, в якому будуть кнопки "почати" і "вийти"
button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(20, 30)) # Increase padding from the bottom

# Кнопка "Почати"
start_button = tk.Button(button_frame, text="Почати", command=start_clicker, bg="#4caf50", fg="white", font=("Trebuchet MS", 12)
                         , bd=0, highlightthickness=0, relief="flat")
start_button.grid(row=0, column=0, padx=10) # Add horizontal padding

# Кнопка "Вийти"
exit_button = tk.Button(button_frame, text="Вийти", command=exit_app, bg="#f44336", fg="white", font=("Trebuchet MS", 12), bd=0, highlightthickness=0, relief="flat")
exit_button.grid(row=0, column=1, padx=10) # Add horizontal padding

root.bind('i', show_info)
keyboard.add_hotkey('esc', exit_app)
root.mainloop()