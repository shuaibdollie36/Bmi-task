
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("BMI Calculator")
window.geometry("1000x800")
heading = Label(window, text=' Body Mass Index Calculator')
heading["font"] = "Ariel" , 30
heading.place(x=250, y=0)
window.configure(bg='yellow')

frame = Frame(window, width=500, height=200, borderwidth=1, relief='ridge')
frame.place(relx=0.15, rely=0.1)

weight = Label(frame, text="Weight(kg):")
weight.place(relx=0, rely=0)
weight_entry = Entry(frame)
weight_entry.place(relx=0.3, rely=0)

height = Label(frame, text="Height(cm):")
height.place(relx=0, rely=0.1)
height_entry = Entry(frame)
height_entry.place(relx=0.2, rely=0.1)

gender = Label(frame, text="Gender:")
gender.place(rely=0.35, relx=0)

age = Label(frame, text="Age:")
age.place(rely=0.6, relx=0)
age_entry = Entry(frame, state='readonly')
age_entry.place(rely=0.6, relx=0.2)

options = ['Select...', 'Male', "Female"]
variable = StringVar(frame)
variable.set(options[0])

def activate(value):
    variable.set(value)
    if value != "Select...":
        age_entry.config(state='normal')
    else:
        age_entry.config(state='readonly')


gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place(relx=0.3, rely=0.4)

def bmi_calc():
    try:
        float(weight_entry.get())
        float(height_entry.get())
        float(age_entry.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + (
                        0.03 * float(age_entry.get())) + 11
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
    except ValueError:
        messagebox.showerror(title=None, message='Gender was not specified or invalid entry was given')
        delete()

calculate = Button(window, text="Calculate your Ideal Body Mass Index", width=50, command=bmi_calc)
calculate.place(rely=0.36, relx=0.2)


bmi = Label(window, text="BMI:")
bmi.place(rely=0.5, relx=0.1)
bmi_field = Entry(window, state='readonly')
bmi_field.place(rely=0.5, relx=0.7)
ideal_bmi = Label(window, text='Ideal BMI:')
ideal_bmi.place(rely=0.5, relx=0.7)
ideal_field = Entry(window, state='readonly')
ideal_field.place(rely=0.5, relx=0.25)


def delete():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.config(state='normal')
    bmi_field.config(state='normal')
    ideal_field.config(state='normal')
    age_entry.delete(0, END)
    bmi_field.delete(0, END)
    ideal_field.delete(0, END)
    age_entry.config(state='readonly')
    bmi_field.config(state='readonly')
    ideal_field.config(state='readonly')
    weight_entry.focus()
    variable.set(options[0])

clear = Button(window, text='Clear', command=delete)
clear.place(rely=0.40, relx=0.1)

exit = Button(window, text='Exit', command='exit')
exit.place(rely=0.40, relx=0.20)

window.mainloop()