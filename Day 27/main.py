from tkinter import *


def miles_to_km():
    miles = float(miles_entry.get())
    kilometer = round(miles*1.609)
    kilometer_result.config(text=str(kilometer))


# Creating a new window and configurations
window = Tk()
window.title("Mile to Km")
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

Kilometer = Label(text="Km")
Kilometer.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)


window.mainloop()
