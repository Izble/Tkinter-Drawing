from tkinter import *
import random

window = Tk()
window.title("Face")

canvas = Canvas(window)
canvas.configure(bg='white')
canvas.pack()

colours = ['yellow', 'blue', 'red', 'green', 'gold']

"""
nts
(..., tags="ect")
"""
txt_1 = canvas.create_text(295, 120, fill="darkblue", font="Times 10 italic bold", text="Left click to colour this face.")
txt_2 = canvas.create_text(295, 135, fill="darkblue", font="Times 10 italic bold", text="Move mouse away to see face.")
face = canvas.create_oval(20, 30, 210, 220, width=2, fill='white')
eye_1 = canvas.create_oval(50, 70, 90, 110, width=2, fill='black')
eye_1_white = canvas.create_oval(75, 75, 85, 85, width=2, fill='white')
eye_2 = canvas.create_oval(140, 70, 180, 110, width=2, fill='black')
eye_2_white = canvas.create_oval(165, 75, 175, 85, width=2, fill='white')
smile = canvas.create_arc(40, 115, 190, 175, start=180, extent=180, fill='black')


def change_colour(event):
    new_colour = random.choice(colours)
    canvas.itemconfig(face, fill=new_colour)


def on_enter(event):
    canvas.itemconfig(txt_1, fill='white')
    canvas.itemconfig(txt_2, fill='white')
    canvas.itemconfig(face, fill='white', outline="")
    canvas.itemconfig(eye_1, fill='white', outline="")
    canvas.itemconfig(eye_1_white, fill='white', outline="")
    canvas.itemconfig(eye_2, fill='white', outline="")
    canvas.itemconfig(eye_2_white, fill='white', outline="")
    canvas.itemconfig(smile, fill='white', outline="")


def on_leave(event):
    canvas.itemconfig(txt_1, fill='darkblue')
    canvas.itemconfig(txt_2, fill='darkblue')
    canvas.itemconfig(face, outline="black")
    canvas.itemconfig(eye_1, fill='black', outline="black")
    canvas.itemconfig(eye_1_white, fill='white', outline="black")
    canvas.itemconfig(eye_2, fill='black', outline="black")
    canvas.itemconfig(eye_2_white, fill='white', outline="black")
    canvas.itemconfig(smile, fill='black', outline="black")


canvas.bind_all('<Button-1>', change_colour)
canvas.bind_all('<Enter>', on_enter)
canvas.bind_all('<Leave>', on_leave)

window.mainloop()
