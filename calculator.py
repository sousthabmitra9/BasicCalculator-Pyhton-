import tkinter as tk
class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, bg, fg,
                 width=60, height=60, radius=30):
        super().__init__(
            parent,
            width=width + 6,
            height=height + 6,
            bg=parent["bg"],
            highlightthickness=0
        )
        self.command = command
        self.bg = bg
        self.fg = fg
        self.text = text
        self.w = width
        self.h = height
        self.r = radius
        self.shadow = self.create_rounded_rect(
            6, 6, width + 2, height + 2, radius,
            fill="#000000", outline=""
        )
        self.button = self.create_rounded_rect(
            2, 2, width, height, radius,
            fill=bg, outline=""
        )
        self.label = self.create_text(
            width // 2,
            height // 2,
            text=text,
            fill=fg,
            font=("Segoe UI", 18, "bold")

        )
        self.bind("<Button-1>", self.animate)

    def create_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1+r, y1, x2-r, y1, x2, y1,
            x2, y1+r, x2, y2-r, x2, y2,
            x2-r, y2, x1+r, y2, x1, y2,
            x1, y2-r, x1, y1+r, x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def animate(self, event):
        # Press animation
        self.move(self.button, 2, 2)
        self.move(self.label, 2, 2)
        self.after(90, self.release)
        self.command()

    def release(self):
        self.move(self.button, -2, -2)
        self.move(self.label, -2, -2)

def press(key):
    if key == "AC":
        display.set("")
    elif key == "=":
        try:
            display.set(eval(display.get()))
        except:
            display.set("Error")
    else:
        display.set(display.get() + key)
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("380x540")
root.configure(bg="#000000")
root.resizable(False, False)
display = tk.StringVar()
entry = tk.Entry(
    root,
    textvariable=display,
    font=("Segoe UI", 42),
    bg="#000000",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)
entry.pack(fill="x", padx=25, pady=(35, 20))
buttons = [
    ["AC", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]
frame = tk.Frame(root, bg="#000000")
frame.pack()
for row in buttons:
    row_frame = tk.Frame(frame, bg="#000000")
    row_frame.pack(pady=8)
    for btn in row:
        if btn in ["+", "-", "*", "/", "="]:
            bg, fg = "#ff9f0a", "white"
        elif btn in ["AC", "%"]:
            bg, fg = "#a5a5a5", "black"
        else:
            bg, fg = "#2c2c2e", "white"

        RoundedButton(
            row_frame,
            btn,
            command=lambda x=btn: press(x),
            bg=bg,
            fg=fg
        ).pack(side="left", padx=8)
root.mainloop()
