import tkinter as tk

last_x = 0
last_y = 0
lesson_canvas = None
lesson_img = None

def start_draw(event):
    global last_x
    global last_y
    last_x = event.x
    last_y = event.y

def draw(event):
    global last_x
    global last_y
    lesson_canvas.create_line(last_x, last_y, event.x, event.y, width=8, fill="blue")
    last_x = event.x
    last_y = event.y

def start_lesson(window):
    global lesson_canvas
    global lesson_img

    for widget in window.winfo_children():
        widget.destroy()

    lesson_canvas = tk.Canvas(window, width=1200, height=800)
    lesson_canvas.pack()

    lesson_img = tk.PhotoImage(file="lesson_bg.png")
    lesson_canvas.create_image(0, 0, image=lesson_img, anchor="nw")

    lesson_canvas.bind("<Button-1>", start_draw)
    lesson_canvas.bind("<B1-Motion>", draw)