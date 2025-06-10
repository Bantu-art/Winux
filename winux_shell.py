# winux_shell.py
import tkinter as tk
import os

def run_command():
    cmd = command_entry.get()
    output_box.insert(tk.END, f"> {cmd}\n")

    if cmd == "pwd":
        output_box.insert(tk.END, os.getcwd() + "\n")
    else:
        output_box.insert(tk.END, "Command not recognized.\n")
    
    command_entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Winux Terminal")
root.geometry("600x400")

# Output display area
output_box = tk.Text(root, bg="black", fg="lime", font=("Consolas", 12))
output_box.pack(expand=True, fill=tk.BOTH)

# Command input
command_entry = tk.Entry(root, bg="black", fg="white", font=("Consolas", 12))
command_entry.pack(fill=tk.X)
command_entry.bind("<Return>", lambda event: run_command())

# Start the terminal window
root.mainloop()
