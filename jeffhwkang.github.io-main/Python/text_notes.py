import tkinter as tk
from tkinter import ttk

import sv_ttk

window = tk.Tk()
window.title("Note Taking App")
window.geometry("720x576")

v_scrollbar = ttk.Scrollbar(window)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

note_entry = tk.Text(window)
note_entry.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

note_entry['yscrollcommand']=v_scrollbar.set
v_scrollbar.config(command=note_entry.yview)

#Run Application
sv_ttk.set_theme("dark")

window.mainloop()