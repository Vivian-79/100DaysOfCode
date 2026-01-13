import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

#label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()#pack our label on the screen

my_label["text"] = "New Text"
my_label.config(text="New Text")


#entry
input = tkinter.Entry(width=10)
input.pack()
input.get()

#button
def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input)
button = tkinter.Button(text="Click Here", command=button_clicked)
button.pack()


new_button = tkinter.Button(text="New Button")
new_button.grid(column=0, row=1)
#error! pack() and grid() are different frames, can't exist at the same time



window.mainloop()