import tkinter as tk
window = tk.Tk()

import lesson

window = None
canvas = None
bg_image = None


def start_screen():
    global window
    global canvas
    global bg_image

    window.geometry("1920x1080")

    bg_image = tk.PhotoImage(file="background.png")

    canvas = tk.Canvas(window, width=1920, height=1080)
    canvas.pack()
    canvas.create_image(0, 0, image=bg_image, anchor="nw")


    canvas.bind("<Button-1>", click)

    window.mainloop()

    canvas = tk.Canvas(window, width=1920, height=1080)
    canvas.pack()
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.bind("<Button-1>", click)

    window.mainloop()


def click(event):
    if 820 <= event.x <= 1100 and 400 <= event.y <= 680:
        start_lesson()


def clear_screen():
    global canvas
    canvas.destroy()


def start_lesson():
    clear_screen()
    lesson.start_lesson(window)