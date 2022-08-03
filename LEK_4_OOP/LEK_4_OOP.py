from tkinter import *

def conversion():
    try:
        if radio_state.get() == 1:
            cel =float(input_entry.get())
            kel= cel + 273.15
            result.config(text=f"{kel} K")
        elif radio_state.get() == 2:
            kel=float(input_entry.get())
            cel= kel - 273.15
            result.config(text=f"{round(cel, 2)} \N{DEGREE SIGN}C")
        elif radio_state.get() == 3:
            fah =float(input_entry.get())
            kel= 5/9*(fah + 459.67)
            result.config(text=f"{round(kel,2)} K")
        elif radio_state.get() == 4:
            kel =float(input_entry.get())
            fah=9/5*(kel - 273.15) + 32
            result.config(text=f"{round(fah,2)} \N{DEGREE SIGN}F")
        elif radio_state.get() == 5:
            cel =float(input_entry.get())
            fah=(9/5*cel) + 32
            result.config(text=f"{round(fah,2)} \N{DEGREE SIGN}F")
        elif radio_state.get() == 6:
            fah =float(input_entry.get())
            cel=(fah -32)*5/9
            result.config(text=f"{round(cel,2)} \N{DEGREE SIGN}C")
        if radio_state.get() not in range(1,7):
            raise Exception
    except ValueError:
        print("Value should be a number.")
    except Exception:
        print("You have to select an option.")

window=Tk()
window.title("Temperature convertor")
window.config(padx=25, pady=25)

input_label = Label(text="Value to convert:")
input_label.grid(column=0, row=1)
input_entry = Entry(width=8)
input_entry.grid(column=1, row=1)
result_label = Label(text="Converted value:")
result_label.grid(column=0, row=2)
result = Label(text="0")
result.grid(column=1, row=2)
convert_button = Button(text="Convert", command=conversion)
convert_button.grid(row=4, columnspan=2)

#Radiobutton

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Celsius to Kelvin", value=1, variable=radio_state)
radiobutton1.grid(column=2, row=0, sticky="W")

radiobutton2 = Radiobutton(text="Kelvin to Celsius", value=2, variable=radio_state)
radiobutton2.grid(column=2, row=1, sticky="W")

radiobutton3 = Radiobutton(text="Fahrenheit to Kelvin", value=3, variable=radio_state)
radiobutton3.grid(column=2, row=2, sticky="W")

radiobutton4 = Radiobutton(text="Kelvin to Fahrenheit", value=4, variable=radio_state)
radiobutton4.grid(column=2, row=3, sticky="W")

radiobutton5 = Radiobutton(text="Celsius to Fahrenheit", value=5, variable=radio_state)
radiobutton5.grid(column=2, row=4, sticky="W")

radiobutton6 = Radiobutton(text="Fahtenheit to Celsius", value=6, variable=radio_state)
radiobutton6.grid(column=2, row=5, sticky="W")


window.mainloop()
