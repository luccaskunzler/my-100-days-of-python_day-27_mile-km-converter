import tkinter

def button_clicked():
    data_miles = float(input.get())
    data_km = data_miles*1.6
    output.config(text=data_km)

window = tkinter.Tk()
window.title("My GUI program")
window.config(padx=20, pady=20)
# Label

input = tkinter.Entry(width=10, font=('Arial', 12, "normal"))
input.grid(row=0, column=1)

miles = tkinter.Label(text="Miles", font=('Arial', 12, "normal"))
miles.grid(row=0, column=2)
# my_label.config(padx=20, pady=20)

is_equal_to = tkinter.Label(text="is equal to", font=('Arial', 12, "normal"))
is_equal_to.grid(row=1, column=0)
# my_label.config(padx=20, pady=20)

km = tkinter.Label(text="Km", font=('Arial', 12, "normal"))
km.grid(row=1, column=2)
# my_label.config(padx=20, pady=20)

output = tkinter.Label(text="0", font=('Arial', 12, "normal"))
output.grid(row=1, column=1)

my_button = tkinter.Button(text="Calculate", font=('Arial', 12, "normal"), command=button_clicked)
my_button.grid(row=2, column=1)
# my_button.config(padx=20, pady=20)


window.mainloop()
