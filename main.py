import tkinter as tk

root = tk.Tk()
root.title("PY Calculator")
root.geometry("400x500")
root.configure(bg="darkgrey")


write = tk.Entry(root)
write.insert(0, "1")
write.pack()

def button_klick(ziffer):
    write.insert(tk.END, ziffer)

button1 = tk.Button(root, text="1", bg="lightgrey", fg="black", font=("Arial", 20), width=4, height=1, highlightbackground="white", highlightcolor="white", command=lambda: button_klick("1"))
button1.pack()

root.mainloop()