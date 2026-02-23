import tkinter as tk
from urllib.request import urlopen
from html.parser import HTMLParser

class SimpleHTMLRenderer(HTMLParser):
    def __init__(self, output_widget):
        super().__init__()
        self.output_widget = output_widget
        self.current_tag = None
        self.font_size_map = {
            'h1': ('Helvetica', 24),
            'h2': ('Helvetica', 20),
            'p': ('Helvetica', 12),
        }

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag.lower()
        font_config = self.font_size_map.get(tag.lower(), ('Helvetica', 12))
        self.output_widget.config(font=font_config)

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        self.output_widget.insert(tk.END, data.strip())
        self.output_widget.insert(tk.END, '\\n\\n') 


def render_html():
    url = entry.get()
    try:
        with urlopen(url) as response:
            html_data = response.read().decode('utf-8')
        
        renderer.feed(html_data)
    except Exception as e:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, f"ERROR: {e}")

root = tk.Tk()
root.title("simple HTML render")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Display", command=render_html)
button.pack(pady=5)

text_area = tk.Text(root, wrap=tk.WORD, height=20, width=80)
text_area.pack(padx=10, pady=10)

renderer = SimpleHTMLRenderer(text_area)

root.mainloop()