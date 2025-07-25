import tkinter as tk
from func_for_l1 import info
import random as r

root = tk.Tk()
root.title("My super program")
root.geometry("231x280")

colors = ["blue", "red", "yellow", "green", "white"]

# ---------- Фрейми ----------
frame1 = tk.Frame(root, bd=2, relief="solid")
frame1.pack(padx=10, pady=10, fill="both", expand=True)

frame2 = tk.Frame(root, bd=2, relief="solid")
frame2.pack(padx=10, pady=10, fill="both", expand=True)

# ---------- Віджети у першому фреймі ----------
label = tk.Label(frame1, text="I love Python",
                 font=("Arial", 30), fg="blue", bg="yellow")
label.pack(pady=10)

entry = tk.Entry(frame1)
entry.pack(pady=5)

def show_text():
    label.config(text=entry.get())

button_show = tk.Button(frame1, text="Push me", command=show_text)
button_show.pack(pady=5)

# ---------- Віджети у другому фреймі ----------
def change_color_label():
    label.config(bg=r.choice(colors))

button_color = tk.Button(frame2, text="Change color", command=change_color_label)
button_color.pack(pady=20)

root.mainloop()
