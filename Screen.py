import tkinter as tk
window = tk.Tk()

def screen():
    background_img ="background.png"
    window.geometry("1920x1080")
    bg_image = tk.PhotoImage(background_img)
    canvas = tk.Canvas(window,width=1920 , height=1080)
    canvas.pack()
    canvas.create_image(0, 0, image=bg_image, anchor="nw")


def click(event):
    if 820 <= event.x <= 1100 and 400 <= event.y <=680 :
        start_lesson()


def clear_screen():
    window.destroy()
    return window


def start_lesson():
    clear_screen()







