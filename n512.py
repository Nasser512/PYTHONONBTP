import tkinter as tk
from pyautocad import Autocad, APoint

class AutoCADLetterDrawer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AutoCAD Letter Drawer")

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.letter_entry = tk.Entry(self.root, width=5)
        self.letter_entry.pack()

        self.draw_button = tk.Button(self.root, text="Draw Letter", command=self.draw_letter)
        self.draw_button.pack()

        self.acad = Autocad(create_if_not_exists=True)

    def draw_letter(self):
        letter = self.letter_entry.get()
        if letter.isalpha() and len(letter) == 1:
            self.draw_on_autocad(letter)
        else:
            print("Please enter a single alphabet letter.")

    def draw_on_autocad(self, letter):
        point = APoint(0, 0)
        self.acad.model.AddText(letter, point, 2.5)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    drawer = AutoCADLetterDrawer()
    drawer.run()
