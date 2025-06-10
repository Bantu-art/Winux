import tkinter as tk
from utils.command_handler import CommandHandler

class Terminal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Winux Terminal")
        self.root.geometry("600x400")
        self.command_handler = CommandHandler()
        self._setup_ui()

    def _setup_ui(self):
        # Output display area
        self.output_box = tk.Text(self.root, bg="black", fg="lime", font=("Consolas", 12))
        self.output_box.pack(expand=True, fill=tk.BOTH)

        # Command input
        self.command_entry = tk.Entry(self.root, bg="black", fg="white", font=("Consolas", 12))
        self.command_entry.pack(fill=tk.X)
        self.command_entry.bind("<Return>", self._handle_command)

    def _handle_command(self, event):
        cmd = self.command_entry.get()
        self.output_box.insert(tk.END, f"> {cmd}\n")
        output = self.command_handler.execute(cmd)
        self.output_box.insert(tk.END, f"{output}\n")
        self.command_entry.delete(0, tk.END)

    def start(self):
        self.root.mainloop()