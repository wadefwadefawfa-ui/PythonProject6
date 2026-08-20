import tkinter as tk
from PIL import Image, ImageTk
import consts
import sound
import time
import random

last_x = 0
last_y = 0
lesson_canvas = None
lesson_img = None
pen_color = consts.PEN_C
pen_size = consts.PEN_S
screen_w = 0
screen_h = 0
img_w = 0
img_h = 0
start_x = 0
start_y = 0
main_window = None
click_count = 0


def close_app(event):
    main_window.destroy()


def handle_click(event):
    global last_x, last_y, pen_color, pen_size, click_count

    x_in = event.x - start_x
    y_in = event.y - start_y

    if 0 <= x_in <= img_w and 0 <= y_in <= img_h:
        real_x = (x_in / img_w) * consts.W
        real_y = (y_in / img_h) * consts.H

        if consts.SEND_X1 < real_x < consts.SEND_X2 and consts.SEND_Y1 < real_y < consts.SEND_Y2:
            last_x = 0
            last_y = 0
            click_count = click_count + 1
            if click_count == 1:
                sound.wrong_answer()
            elif click_count == 2:
                sound.good_spell()
            elif click_count == 3:
                sound.try_again()
            elif click_count == 4:
                sound.good_break()
                click_count = 0

        elif consts.ERASER_X1 < real_x < consts.ERASER_X2 and consts.ERASER_Y1 < real_y < consts.ERASER_Y2:
            lesson_canvas.delete("drawing")
            last_x = 0
            last_y = 0

        elif consts.PEN_X1 < real_x < consts.PEN_X2 and consts.PEN_Y1 < real_y < consts.PEN_Y2:
            pen_color = consts.PEN_C
            pen_size = consts.PEN_S
            last_x = 0
            last_y = 0

        elif consts.BOARD_X1 < real_x < consts.BOARD_X2 and consts.BOARD_Y1 < real_y < consts.BOARD_Y2:
            last_x = event.x
            last_y = event.y


def draw(event):
    global last_x, last_y

    x_in = event.x - start_x
    y_in = event.y - start_y

    if 0 <= x_in <= img_w and 0 <= y_in <= img_h:
        real_x = (x_in / img_w) * consts.W
        real_y = (y_in / img_h) * consts.H

        if consts.BOARD_X1 < real_x < consts.BOARD_X2 and consts.BOARD_Y1 < real_y < consts.BOARD_Y2:
            if not (consts.SEND_X1 < real_x < consts.SEND_X2 and consts.SEND_Y1 < real_y < consts.SEND_Y2):
                if last_x != 0 and last_y != 0:
                    lesson_canvas.create_line(last_x, last_y, event.x, event.y, width=pen_size, fill=pen_color,
                                              capstyle=tk.ROUND, smooth=True, tags="drawing")
                last_x = event.x
                last_y = event.y


def stop_draw(event):
    global last_x, last_y
    last_x = 0
    last_y = 0


def start_lesson(window, w, h):
    global lesson_canvas, lesson_img, screen_w, screen_h, main_window
    global img_w, img_h, start_x, start_y

    main_window = window
    screen_w = w
    screen_h = h

    img = Image.open(consts.LESSON_PIC)

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

    lesson_canvas = tk.Canvas(window, width=screen_w, height=screen_h, highlightthickness=0, bg=consts.BG_COLOR)
    lesson_canvas.pack()

    img = img.resize((img_w, img_h))
    lesson_img = ImageTk.PhotoImage(img)
    lesson_canvas.create_image(start_x, start_y, image=lesson_img, anchor="nw")

    lesson_canvas.bind("<Button-1>", handle_click)
    lesson_canvas.bind("<B1-Motion>", draw)
    lesson_canvas.bind("<ButtonRelease-1>", stop_draw)
    main_window.bind("<Escape>", close_app)

    sound.first_task()