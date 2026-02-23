import tkinter as tk
from tkinter import scrolledtext
from urllib.request import urlopen

def load_and_display():

    url = entry.get()
    
    try:
        with urlopen(url) as response:
            html_data = response.read().decode('utf-8')
        
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, html_data)
    except Exception as e:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, f"ERROR: {e}")

root = tk.Tk()
root.title("page loader")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Ввод", command=load_and_display)
button.pack(pady=5)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=80)
text_area.pack(padx=10, pady=10)

root.mainloop()