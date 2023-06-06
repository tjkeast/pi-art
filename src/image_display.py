from tkinter import *
from PIL import ImageTk, Image
import logging as log


class ImageDisplay:
    def __init__(self, cycle_frequency_ms: int = 1000) -> None:
        self.image_paths = []
        self.cycle_frequency_ms = cycle_frequency_ms
        self.win = Tk()
        self.win.title("pi-art")
        self.win.geometry("1920x1080")

        self.frame = Frame(self.win, width=600, height=400)
        self.frame.pack()
        self.frame.place(anchor=CENTER, relx=0.5, rely=0.5)

        self.current_image = None
        self.panel = Label()
        self.panel.pack()
        self.next_image()

    def start(self) -> None:
        self.win.attributes("-fullscreen", True)
        self.win.mainloop()

    def add_image(self, image_path: str) -> None:
        self.image_paths.append(image_path)
        log.debug("Image display added new image %s" % image_path)

    def load_image(self, image_path: str) -> ImageTk.PhotoImage:
        return ImageTk.PhotoImage(Image.open(image_path))

    def render(self, image_path) -> None:
        img = self.load_image(image_path)
        self.current_image = image_path
        self.panel.img = img
        self.panel["image"] = img

    def next_image(self) -> None:
        self.panel.after(self.cycle_frequency_ms, self.next_image)

        if len(self.image_paths) == 0:
            return

        index = (
            self.image_paths.index(self.current_image)
            if self.current_image != None
            else -1
        )
        if index + 1 >= len(self.image_paths):
            index = 0
        else:
            index += 1

        self.render(self.image_paths[index])
