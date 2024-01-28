import tkinter as tk

root = tk.Tk()
root.title = "TMCalculator"

def TableMaker():
    try:
        N = int(entry_N.get())
        M = int(entry_M.get())
        text.delete(1.0, tk.END)
        for i in range(1, M + 1):
            text.insert(tk.END, f"{N} X {i} = {N * i}\n")
    except:
        text.delete(1.0, tk.END)
        text.insert(tk.END, f"This is not a integer!")

label_N = tk.Label(root, text="Enter a number = ")
label_N.grid(row=0, column=0)

entry_N = tk.Entry(root)
entry_N.grid(row=0, column=1)

label_M = tk.Label(root, text="Enter the multiplier = ")
label_M.grid(row=1, column=0)

entry_M = tk.Entry(root)
entry_M.grid(row=1, column=1)

button = tk.Button(root, text="Make Table", command=TableMaker)
button.grid(row=2, column=0, columnspan=2)

def add():
    try:
        NoA = int(e_NoA.get())
        NoA2 = int(e_NoA2.get())
        text.delete(1.0, tk.END)
        text.insert(tk.END, f"{NoA + NoA2}")
    except:
        text.delete(1.0, tk.END)
        text.insert(tk.END, f"This is not a integer!")

l_NoA = tk.Label(root, text="Insert a number = ")
l_NoA.grid(row=3, column=0)

e_NoA = tk.Entry(root)
e_NoA.grid(row=3, column=1)

l_NoA2 = tk.Label(root, text="Insert a number you want to add it with = ")
l_NoA2.grid(row=4, column=0)

e_NoA2 = tk.Entry(root)
e_NoA2.grid(row=4, column=1)

button1 = tk.Button(root, text="Add", command=add)
button1.grid(row=5, column=0, columnspan=2)

def subtract():
    try:
        NoS = int(e_NoS.get())
        NoS2 = int(e_NoS2.get())
        text.delete(1.0, tk.END)
        text.insert(tk.END, f"{NoS - NoS2}")
    except:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "This is not an integer!")

l_NoS = tk.Label(root, text="Insert a number = ")
l_NoS.grid(row=6, column=0)

e_NoS = tk.Entry(root)
e_NoS.grid(row=6, column=1)

l_NoS2 = tk.Label(root, text="Insert a number you want to subtract from it = ")
l_NoS2.grid(row=7, column=0)

e_NoS2 = tk.Entry(root)
e_NoS2.grid(row=7, column=1)


button2 = tk.Button(root, text="Subtract", command=subtract)
button2.grid(row=8, column=0, columnspan=2)

def multiply():
    try:
        NoM = int(e_NoM.get())
        NoM2 = int(e_NoM2.get())
        text.delete(1.0, tk.END)
        text.insert(tk.END, f"{NoM * NoM2}")
    except:
        text.delete(1.0, tk.END)
        text.insert(tk.END, f"This is not a integer!")

l_NoM = tk.Label(root, text="Insert a number = ")
l_NoM.grid(row=9, column=0)

e_NoM = tk.Entry(root)
e_NoM.grid(row=9, column=1)

l_NoM2 = tk.Label(root, text="Insert a number you want to multiply it with = ")
l_NoM2.grid(row=10, column=0)

e_NoM2 = tk.Entry(root)
e_NoM2.grid(row=10, column=1)

button3 = tk.Button(root, text="Multiply", command=multiply)
button3.grid(row=11, column=0, columnspan=2)

def divide():
    try:
        NoD = int(e_NoD.get())
        NoD2 = int(e_NoD2.get())
        text.delete(1.0, tk.END)
        text.insert(tk.END, f"{NoD / NoD2}")
    except:
        text.delete(1.0, tk.END)
        text.insert(tk.END, f"This is not a integer!")

l_NoD = tk.Label(root, text="Insert a number = ")
l_NoD.grid(row=12, column=0)

e_NoD = tk.Entry(root)
e_NoD.grid(row=12, column=1)

l_NoD2 = tk.Label(root, text="Insert a number you want to divide it with = ")
l_NoD2.grid(row=13, column=0)

e_NoD2 = tk.Entry(root)
e_NoD2.grid(row=13, column=1)

button4 = tk.Button(root, text="Divide", command=divide)
button4.grid(row=14, column=0, columnspan=2)

text = tk.Text(root)
text.grid(row=15, column=0, columnspan=2)

root.mainloop()
