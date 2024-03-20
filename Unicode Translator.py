import tkinter as tk
from tkinter import ttk, messagebox

def hex_to_utf(hex_input, conversion_type):
    try:
        decimal_value = int(hex_input, 16)
        if conversion_type == "Unicode":
            utf_result = hex(decimal_value)[2:]
        elif conversion_type == "Utf-8 to Hex":
            utf_result = hex(decimal_value)[2:]
        elif conversion_type == "Utf-16 to Hex":
            utf_result = hex(decimal_value)[2:]
        elif conversion_type == "Utf-32 to Hex":
            utf_result = hex(decimal_value)[2:]
        return decimal_value, utf_result
    except ValueError:
        return None, None

def utf_to_hex(utf_input, conversion_type):
    try:
        decimal_value = int(utf_input, 16)
        if conversion_type == "Utf-8 to Hex":
            hex_result = chr(decimal_value).encode('utf-8').hex()
        elif conversion_type == "Utf-16 to Hex":
            hex_result = chr(decimal_value).encode('utf-16').hex()
        elif conversion_type == "Utf-32 to Hex":
            hex_result = chr(decimal_value).encode('utf-32').hex()
        return hex_result
    except ValueError:
        return None

def validate_hex_input(text):
    if text == '':
        return True  # Allow empty string
    if text.startswith('0x') or text.startswith('0X'):
        text = text[2:]
    return all(c.upper() in '0123456789ABCDEF' for c in text)

def validate_utf_input(text):
    if text == '':
        return True  # Allow empty string
    try:
        int(text, 16)
        return True
    except ValueError:
        return False

def process_input():
    input_value = entry_input.get()
    conversion_type = conversion_var.get()
    if conversion_type == "Unicode":
        # Perform Unicode conversion
        if validate_utf_input(input_value):
            entry_input.delete(0, tk.END)  # Clear input textbox after conversion
            hex_result = input_value
            add_to_history(input_value, hex_result)
        else:
            messagebox.showerror("Error", "Invalid input! Please enter a valid hexadecimal value.")
    else:
        # Perform UTF to Hex conversion
        if validate_utf_input(input_value):
            entry_input.delete(0, tk.END)  # Clear input textbox after conversion
            hex_result = utf_to_hex(input_value, conversion_type)
            if hex_result is not None:
                add_to_history(input_value, hex_result)
            else:
                messagebox.showerror("Error", "Invalid UTF input!")
        else:
            messagebox.showerror("Error", "Invalid input! Please enter a valid hexadecimal value.")

def add_to_history(input_value, result):
    history.append((input_value, result))
    update_table()

def update_table():
    table.delete(*table.get_children())
    if conversion_var.get() == "Unicode":
        table['columns'] = ("HEX", "UTF-8", "UTF-16", "UTF-32")
        table.heading("HEX", text="HEX")
        table.heading("UTF-8", text="UTF-8")
        table.heading("UTF-16", text="UTF-16")
        table.heading("UTF-32", text="UTF-32")
    else:
        table['columns'] = ("Input", "Result")
        table.heading("Input", text="Input")
        table.heading("Result", text="Result")
    for item in history:
        table.insert("", "end", values=item)

def reset_table():
    history.clear()
    table.delete(*table.get_children())

history = []

window = tk.Tk()
window.title("UNICODE CONVERTER")

label_title = tk.Label(window, text="UNICODE CONVERTER", font=("Helvetica", 30))
label_title.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

label_group = tk.Label(window, text="GROUP 9: CABUNGCAL, DIAZ, GUILLARTE, NGO, SO", font=("Helvetica", 10))
label_group.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

entry_input = tk.Entry(window, font=("Helvetica", 10)) 
entry_input.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

# Radio buttons for conversion type selection
conversion_var = tk.StringVar()
conversion_var.set("Unicode") 
conversion_choices = ["Unicode", "Utf-8 to Hex", "Utf-16 to Hex", "Utf-32 to Hex"]
for i, choice in enumerate(conversion_choices):
    radio_button = tk.Radiobutton(window, text=choice, variable=conversion_var, value=choice)
    radio_button.grid(row=3, column=i, padx=(10, 5), pady=5, sticky="w")


button_convert = tk.Button(window, text="Convert", command=process_input, width=7) 
button_convert.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

table = ttk.Treeview(window, show="headings")
table.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

button_reset = tk.Button(window, text="Reset", command=reset_table, width=7)
button_reset.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

window.mainloop()
