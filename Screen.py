import tkinter as tk


window = tk.Tk()
window.geometry("1920x1080")
# bg = tk.PhotoImage(file="bg_image.jpeg")
canvas = tk.Canvas(window,width=1920 , height=1080)
canvas.pack()
bg_image = tk.PhotoImage(file="background.png")
canvas.create_image(0, 0, image=bg_image, anchor="nw")

def click(event):
    if 820 <= event.x <= 1100 and 400 <= event.y <=680 :
        start_lesson()

def clear_screen():
    window.destroy()

def start_lesson():
    clear_screen()







