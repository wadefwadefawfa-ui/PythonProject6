import tkinter as tk
from PIL import Image, ImageTk
import lesson
import consts

window = None
canvas = None
bg_image = None
screen_w = 0
screen_h = 0
img_w = 0
img_h = 0
start_x = 0
start_y = 0


def start_screen():
    global window, canvas, bg_image, screen_w, screen_h, img_w, img_h, start_x, start_y

    window = tk.Tk()
    window.attributes('-fullscreen', True)

    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()

    img = Image.open(consts.MAIN_PIC)

    ratio = consts.W / consts.H
    screen_ratio = screen_w / screen_h

    if screen_ratio > ratio:
        img_h = screen_h
        img_w = int(img_h * ratio)
    else:
        img_w = screen_w
        img_h = int(img_w / ratio)

    start_x = int((screen_w - img_w) / 2)
    start_y = int((screen_h - img_h) / 2)

    img = img.resize((img_w, img_h))
    bg_image = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(window, width=screen_w, height=screen_h, highlightthickness=0, bg=consts.BG_COLOR)
    canvas.pack()
    canvas.create_image(start_x, start_y, image=bg_image, anchor="nw")

    canvas.bind("<Button-1>", click)
    window.bind("<Escape>", close_app)

    window.mainloop()


def close_app(event):
    window.destroy()


def click(event):
    x_in = event.x - start_x
    y_in = event.y - start_y

    if 0 <= x_in <= img_w and 0 <= y_in <= img_h:
        real_x = (x_in / img_w) * consts.W
        real_y = (y_in / img_h) * consts.H

        print("X:", real_x, "Y:", real_y)

        if consts.GREEN_BTN_X1 <= real_x <= consts.GREEN_BTN_X2 and consts.GREEN_BTN_Y1 <= real_y <= consts.GREEN_BTN_Y2:
            start_lesson()


def clear_screen():
    canvas.destroy()


def start_lesson():
    clear_screen()
    lesson.start_lesson(window, screen_w, screen_h)