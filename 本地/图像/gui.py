import tkinter as tk
from tkinter import colorchooser
from image_creation import create_blank_image, save_image
from effects import apply_linear_gradient

def start_gui():
    root = tk.Tk()
    root.title("Image Creator")

    def create_image():
        width = int(width_entry.get())
        height = int(height_entry.get())
        color = colorchooser.askcolor()[1]
        image = create_blank_image(width, height, color)
        image = apply_linear_gradient(image, (255, 0, 0), (0, 0, 255))
        save_image(image, "output.png", "PNG")

    width_label = tk.Label(root, text="Width:")
    width_label.pack()
    width_entry = tk.Entry(root)
    width_entry.pack()

    height_label = tk.Label(root, text="Height:")
    height_label.pack()
    height_entry = tk.Entry(root)
    height_entry.pack()

    create_button = tk.Button(root, text="Create Image", command=create_image)
    create_button.pack()

    root.mainloop()