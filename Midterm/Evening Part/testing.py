from tkinter import ttk, Tk, StringVar

parent = Tk()

release = StringVar()
ra = ttk.Radiobutton(parent, text="Alpha", variable=release, value=0)
rb = ttk.Radiobutton(parent, text="Beta", variable=release, value=1)
rp = ttk.Radiobutton(parent, text="Prod", variable=release, value=2)

ra.pack()
rb.pack()
rp.pack()

parent.mainloop()
