import tkinter as tk
from tkinter import messagebox

def check_script_for_threats(script_text):
    dangerous_keywords = [
        'eval',
        'exec',
        'os.system',
        '__import__',
        'subprocess.run',
        'shutil.copy',
        'open',
        'read',
        'write'
    ]

    for keyword in dangerous_keywords:
        if keyword in script_text:
            return True
    return False

def analyze_script():
    user_input = input_field.get("1.0", tk.END).strip()
    if check_script_for_threats(user_input):
        messagebox.showwarning("WARNING", "Potentially dangerous structures detected!")
    else:
        messagebox.showinfo("Result", "The script appears to be secure.")

root = tk.Tk()
root.title("script analyzer")

input_label = tk.Label(root, text="Paste your script here:")
input_label.pack()

input_field = tk.Text(root, height=10, width=50)
input_field.pack()

analyze_button = tk.Button(root, text="Check", command=analyze_script)
analyze_button.pack()

root.mainloop()

#This program does not guarantee protection against real threats and is intended solely to demonstrate the principles of potential risk analysis. True protection is provided by comprehensive antivirus systems and process behavior monitoring.