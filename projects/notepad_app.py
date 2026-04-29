import tkinter as tk
from tkinter import Tk, Text, Frame, Button


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("My Notepad")

        # Text Widget
        self.text_area: Text = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        # let's build Frames to hold buttons
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # save button
        self.save_button: Button = Button(self.button_frame, text='Save Note', command=self.save_file)

    def save_file(self) -> None:
        pass

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()


if __name__ == '__main__':
    main()
