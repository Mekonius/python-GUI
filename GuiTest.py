import tkinter as tk
import tkinter.ttk as tkk

window = tk.Tk()

message = tkk.Label(window, text="Hello, world!")

label = tkk.Label(window, text="Enter a name:")
label2 = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=0
)
text = tk.Text(window, height=1, width=20, foreground="orange", background="black")
entry = tk.Entry(fg="orange", bg="black", width=50)

btn = tkk.Button(window, text="Click me!")

Alert = entry.get()


frame = tk.Frame(window)
message.pack()
label.pack()
label2.pack()
entry.pack()
btn.pack()

window.mainloop()