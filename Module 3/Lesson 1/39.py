import tkinter as tk
import random as r

root = rofls_weather = [
    "сьогодні ливень треба мабуть в макдональдс з'їздити"
    "Не зробив домашку, бо мій хом’як вивчив Python і стер файл."
    "Сьогодні викладач настрій має як буря в пустелі. Удачі!"
    "Не можеш вирішити проблему – зроби вигляд, що це фіча."
    "Сьогодні Меркурій у відкаті. Не коміть в master!"
    "Настрій: як у Wi-Fi в метро – нестабільний."
]

root = tk.Tk()

root.title("Жартівливий Генератор Погоди")

root.geometry("400x600")

label = tk.Label(root, text="I love Python",
                 font=("Arial", 30), fg="#14DB68", bg="#8914DB", pady=200, padx=200)
label.pack(pady=30, side="right", fill="both")

button = tk.Button(root, text="Дізнатись погоду", font=("Arial", 30), command=rofls_weather, bg="#DB9826", fg="#14DB68")
button.pack(side="left", fill="both")
def genarator_weather():
    label.config(text =r.choice(rofls_weather))

tk.mainloop()