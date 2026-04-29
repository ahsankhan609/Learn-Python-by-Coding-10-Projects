import tkinter as tk
from tkinter import Tk, Text, Frame, Button, filedialog, messagebox


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("My Notepad")
        self.root.geometry("600x400")

        # Track the current file path
        self.current_file: str | None = None
        self.is_modified: bool = False

        # Text Widget
        self.text_area: Text = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        # Bind text modification detection
        self.text_area.bind("<<Change>>", self._on_text_change)
        self.text_area.bind("<KeyRelease>", self._on_text_change)

        # Build Frame to hold buttons
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack(pady=5)

        # Save button
        self.save_button: Button = Button(self.button_frame, text='Save Note', command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=5)

        # Load button
        self.load_button: Button = Button(self.button_frame, text='Load Note', command=self.load_file)
        self.load_button.pack(side=tk.LEFT, padx=5)

        # New button
        self.new_button: Button = Button(self.button_frame, text='New Note', command=self.new_file)
        self.new_button.pack(side=tk.LEFT, padx=5)

        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _on_text_change(self, event=None) -> None:
        """Track if text has been modified."""
        self.is_modified = True

    def _on_closing(self) -> None:
        """Handle window closing with unsaved changes warning."""
        if self.is_modified:
            response = messagebox.askyesnocancel(
                "Unsaved Changes",
                "You have unsaved changes. Do you want to save before closing?"
            )
            if response is None:  # Cancel
                return
            elif response:  # Yes
                self.save_file()
        self.root.destroy()

    def save_file(self) -> None:
        """Save file to current path or ask for new path if no file is open."""
        try:
            if self.current_file is None:
                # No file is currently open, ask user for a new file
                file_path: str | None = filedialog.asksaveasfilename(
                    defaultextension='.txt',
                    filetypes=[('Text File', '*.txt'), ('All Files', '*.*')]
                )

                if not file_path:  # User cancelled
                    return

                self.current_file = file_path

            # Write to the current file
            with open(self.current_file, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

            self.is_modified = False
            self.root.title(f"My Notepad - {self.current_file}")
            messagebox.showinfo("Success", f"File saved to: {self.current_file}")
            print(f"File saved to: {self.current_file}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")
            print(f"Error saving file: {e}")

    def load_file(self) -> None:
        """Load a file into the text area."""
        try:
            file_path: str | None = filedialog.askopenfilename(
                defaultextension='.txt',
                filetypes=[('Text File', '*.txt'), ('All Files', '*.*')]
            )

            if not file_path:  # User cancelled
                return

            with open(file_path, 'r') as file:
                content: str = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)

            self.current_file = file_path
            self.is_modified = False
            self.root.title(f"My Notepad - {self.current_file}")
            messagebox.showinfo("Success", f"File loaded from: {self.current_file}")
            print(f"File loaded from: {self.current_file}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")
            print(f"Error loading file: {e}")

    def new_file(self) -> None:
        """Create a new file."""
        if self.is_modified:
            response = messagebox.askyesnocancel(
                "Unsaved Changes",
                "You have unsaved changes. Do you want to save before creating a new file?"
            )
            if response is None:  # Cancel
                return
            elif response:  # Yes
                self.save_file()

        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.is_modified = False
        self.root.title("My Notepad")

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()


if __name__ == '__main__':
    main()
