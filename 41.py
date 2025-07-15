from tkinter import Tk, Label, Button, Entry

# Створення головного вікна
root = Tk()
root.title("Приклади place")
root.geometry("400x300")  # Ширина × Висота

#root.resizable(True, False)

root.minsize(600, 600)            # не менше 600 px
root.maxsize(1000, 1000)           # не більше 1000 px


# Додавання лейблів
Label(root, text="Мітка 1", width=15, height=2, font=("Arial", 14)).place(x=20, y=50)
Label(root, text="Центр", width=15, height=2, font=("Arial", 14)).place(relx=0.5, rely=0.2, anchor="center")
Label(root, text="Мітка 3", width=15, height=2, font=("Arial", 14)).place(x=150, y=100)

# Додавання поля введення
Entry(root, width=20, font=("Arial", 14)).place(relx=0.5, rely=0.5, anchor="center")  # Центровано по відношенню до вікна

# Додавання кнопок
Button(root, text="Кнопка 1", width=15, font=("Arial", 14)).place(x=50, y=200)
Button(root, text="Кнопка 2", width=15, font=("Arial", 14)).place(relx=0.5, rely=0.7, anchor="center")

# Запуск головного циклу
root.mainloop()
