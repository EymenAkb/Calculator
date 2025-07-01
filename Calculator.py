import tkinter as tk

class calculator:
    def mult():
        a = entry1.get()
        b = entry2.get()
        try:
            c = int(a)*int(b)
            lans.configure(text=f"answer: {c}")
        except ValueError:
            lans.configure(text="there is no number")

    def add():
        a = entry1.get()
        b = entry2.get()
        try:
            c = int(a)+int(b)
            lans.configure(text=f"answer: {c}")
        except ValueError:
            lans.configure(text="there is no number")

    def sub():
        a = entry1.get()
        b = entry2.get()
        try:
            c = int(a)-int(b)
            lans.configure(text=f"answer: {c}")
        except ValueError:
            lans.configure(text="there is no number")

    def div():
        a = entry1.get()
        b = entry2.get()
        try:
            c = int(a)/int(b)
            lans.configure(text=f"answer: {c}")
        except ValueError:
            lans.configure(text="there is no number")
        except ZeroDivisionError:
            lans.configure(text="input is zero")


calc = calculator

pencere = tk.Tk()
pencere.title("calculator")
pencere.configure(bg="black", width=1000, height=1000)

label = tk.Label(text="Welcome", bg="white")
label.pack()

entry1 = tk.Entry(bg="white")
entry1.pack()

entry2 = tk.Entry(bg="white")
entry2.pack()

frame = tk.Frame(pencere, bg="black").pack()

bmult = tk.Button(frame, text="*", bg="white", command=calc.mult)
bmult.pack(side="left", padx=5)

bbol = tk.Button(frame, text="/", bg="white", command=calc.div)
bbol.pack(side="left", padx=5)

bsub = tk.Button(frame, text="-", bg="white", command=calc.sub)
bsub.pack(side="left", padx=5)

badd = tk.Button(frame, text="+", bg="white", command=calc.add)
badd.pack(side="left", padx=5)

lans = tk.Label(text="answer:", bg="white")
lans.pack()

pencere.mainloop()