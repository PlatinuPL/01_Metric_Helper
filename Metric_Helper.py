from email.mime import base
import tkinter
from tkinter import StringVar, ttk, END

# Define window
root = tkinter.Tk()
root.iconbitmap("ruler.ico")
root.title("Metric Helper!")
root.resizable(0,0)

# Define fonts and colors
field_font = ("Cambria", 10)
bg_color = "#c75c5c"
button_color = "#f5cf87"
root.config(bg = bg_color)

# Define Functions
def convert():
    metric_value = {
        "femto":10**-15, 
        'pico':10**-12, 
        'nano':10**-9, 
        'micro':10**-6, 
        'mili':10**-3, 
        'centi':10**-2, 
        'deci':10**-1, 
        'base value':10**0, 
        'deca':10**1, 
        'hecto':10**2, 
        'kilo':10**3, 
        'mega':10**6,
        'giga':10**9,
        'tera':10**12,
        'peta':10**15
    }

    output_field.delete(0,END)

    # Get all user information
    start_value = float(input_field.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get() 

    base_value = start_value*metric_value[start_prefix]

    end_value = base_value/metric_value[end_prefix]

    output_field.insert(0, str(end_value))
# Define Layout

# Create the input and output entry fields
input_field = tkinter.Entry(root, width=20, font=field_font)
output_field = tkinter.Entry(root, width=20, font=field_font)
equal_label = tkinter.Label(root, text = "=", font = field_font, bg = bg_color)

input_field.grid(row = 0, column=0, padx = 20, pady = 20)
equal_label.grid(row = 0, column=1)
output_field.grid(row = 0, column=2, padx = 20, pady = 20)

input_field.insert(0, "Enter your quantity")

#Create dropdowns for metric values
metric_list = ["femto", 'pico', 'nano', 'micro', 'mili', 'centi', 'deci', 'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']
input_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify="center")
output_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify="center")



"""input_choice = StringVar()
output_choice = StringVar()
input_dropdown = tkinter.OptionMenu(root, input_choice, *metric_list)
output_dropdown = tkinter.OptionMenu(root, output_choice, *metric_list)
"""
to_label = tkinter.Label(root, text = "to", font = field_font, bg = bg_color)

input_combobox.grid(row=1, column=0)
to_label.grid(row=1,column=1)
output_combobox.grid(row=1,column=2)

input_combobox.set('base value')
output_combobox.set('base value')

#Create a conversion button
convert_button = tkinter.Button(root, text = "Convert", font = field_font, bg = button_color, command=convert)
convert_button.grid(row=2,column=0,padx=20,pady=20, columnspan=3)


# Run to root main loop
root.mainloop()