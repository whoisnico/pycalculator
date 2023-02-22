import tkinter as tk

root = tk.Tk()
root.title("PY Calculator")
root.geometry("400x500")
root.configure(bg="darkgrey")


write = tk.Entry(root)
write.insert(0, "")
write.pack()

def button_klick(ziffer):
    write.insert(tk.END, ziffer)

def result():
    result = eval(write.get())
    write.delete(0, tk.END)
    write.insert(0, result)
    

button1 = tk.Button(root, text="1", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("1"))
button1.pack()

button1 = tk.Button(root, text="=", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=10, command=result)
button1.pack()

root.mainloop()