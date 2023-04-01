import tkinter as tk

root = tk.Tk()
root.title("PY Calculator")
root.geometry("400x500")
root.configure(bg="darkblue")


write = tk.Entry(root)
write.insert(0, "")
write.pack()

def button_klick(ziffer):
    write.insert(tk.END, ziffer)

def result():
    try:
        result = eval(write.get())
        write.delete(0, tk.END)
        write.insert(0, result)
    except:
        write.delete(0, tk.END)
        write.insert(0, "Math Error")
    

button1 = tk.Button(root, text="1", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("1"))
button1.pack()

button2 = tk.Button(root, text="2", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("2"))
button2.pack()

button3 = tk.Button(root, text="3", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("3"))
button3.pack()

button4 = tk.Button(root, text="4", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("4"))
button4.pack()

button5 = tk.Button(root, text="5", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("5"))
button5.pack()

button6 = tk.Button(root, text="6", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("6"))
button6.pack()

button7 = tk.Button(root, text="7", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("7"))
button7.pack()

button8 = tk.Button(root, text="8", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("8"))
button8.pack()

button9 = tk.Button(root, text="9", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("9"))
button9.pack()

button0 = tk.Button(root, text="0", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("0"))
button0.pack()

buttonadd = tk.Button(root, text="+", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("+"))
buttonadd.pack()

buttonsub = tk.Button(root, text="-", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=lambda: button_klick("-"))
buttonsub.pack()

buttonresult = tk.Button(root, text="=", bg="grey", font=("Arial", 20), width=4, height=1, borderwidth=0, command=result)
buttonresult.pack()

button1.place(x=50, y=50)
button2.place(x=100, y=50)
button3.place(x=150, y=50)
button4.place(x=50, y=100)
button5.place(x=100, y=100)
button6.place(x=150, y=100)
button7.place(x=50, y=150)
button8.place(x=100, y=150)
button9.place(x=150, y=150)
button0.place(x=100, y=200)
buttonsub.place(x=50, y=200)
buttonadd.place(x=150, y=200)
buttonresult.place(x=100, y=250)

root.mainloop()