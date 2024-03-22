import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def hex_to_utf(utf_input, conversion_type):
    try:
        decimal_value = int(utf_input, 16)
        if conversion_type == "Hex to Utf-8":
            utf_result = chr(decimal_value).encode('utf-8').hex().upper()
        elif conversion_type == "Hex to Utf-16":
            utf_result = chr(decimal_value).encode('utf-16be').hex().upper()
        elif conversion_type == "Hex to Utf-32":
            utf_result = chr(decimal_value).encode('utf-32be').hex().upper()
        return utf_result
    except ValueError:
        return None

def utf_to_hex(hex_input, conversion_type):
    try:
        decimal_value = int(hex_input, 16)
        if conversion_type == "Utf-8 to Hex":
            hex_result = bytes([decimal_value]).decode('utf-8').encode('utf-8').hex().upper()
        elif conversion_type == "Utf-16 to Hex":
            hex_result = bytes([decimal_value]).decode('utf-16').encode('utf-16').hex().upper()
        elif conversion_type == "Utf-32 to Hex":
            hex_result = bytes([decimal_value]).decode('utf-32').encode('utf-32').hex().upper()
        return hex_result
    except ValueError:
        return None

def validate_hex_input(text):
    if text == '':
        return False  # Do not allow empty string
    if text.startswith('0x') or text.startswith('0X'):
        text = text[2:]
    return all(c.upper() in '0123456789ABCDEF' for c in text) and len(text) <= 8

def validate_utf_input(text):
    if text == '':
        return False  # Do not allow empty string
    return all(c.upper() in '0123456789ABCDEF' for c in text) and len(text) <= 8

def convert_input():
    result_text = process_input(True)
    if result_text is not None:
        save_to_file(result_text)

def translate_input():
    result_text = process_input(False)
    if result_text is not None:
        save_to_file(result_text)

def process_input(isConvert):
    input_value = entry_input.get().upper()
    if isConvert:
        if validate_hex_input(input_value):
            utf_result = hex_to_utf(input_value, conversion_var.get())
            add_to_history(input_value, utf_result)
            return utf_result
        else:
            messagebox.showerror("Error", "Invalid input! Please enter a valid hexadecimal value.")
    else:
        if validate_utf_input(input_value):
            hex_result = utf_to_hex(input_value, translation_var.get())
            if hex_result is not None:
                add_to_history(input_value, hex_result)
                return hex_result
            else:
                messagebox.showerror("Error", "Invalid UTF input!")
        else:
            messagebox.showerror("Error", "Invalid input! Please enter a valid UTF value.")

def add_to_history(input_value, result):
    history.append((input_value, result))
    update_table()

def update_table():
    table.delete(*table.get_children())
    table['columns'] = ("Input", "Result")
    table.heading("Input", text="Input")
    table.heading("Result", text="Result")
    for item in history:
        table.insert("", "end", values=item)

def reset_table():
    history.clear()
    table.delete(*table.get_children())


def save_to_file(result_text):
    file_path = "output.txt"
    with open(file_path, "a") as file:  # Open the file in append mode
        file.write(result_text + "\n")   # Append the new result followed by a newline character
    messagebox.showinfo("File Updated", "Result appended to {}".format(file_path))
    
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

conversion_choices = ["Hex to Utf-8", "Hex to Utf-16", "Hex to Utf-32"]

for i, choice in enumerate(conversion_choices):
    radio_button = tk.Radiobutton(window, text=choice, variable=conversion_var, value=choice)
    radio_button.grid(row=3, column=i, padx=(10, 5), pady=5, sticky="w")

button_convert = tk.Button(window, text="Convert", command=convert_input, width=7) 
button_convert.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

# Radio buttons for translation type selection
translation_var = tk.StringVar()

translation_choices = ["Utf-8 to Hex", "Utf-16 to Hex", "Utf-32 to Hex"]
for i, choice in enumerate(translation_choices):
    radio_button = tk.Radiobutton(window, text=choice, variable=translation_var, value=choice)
    radio_button.grid(row=5, column=i, padx=(10, 5), pady=5, sticky="w")

button_translate = tk.Button(window, text="Translate", command=translate_input, width=7) 
button_translate.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

table = ttk.Treeview(window, show="headings")
table.grid(row=7, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

button_reset = tk.Button(window, text="Reset", command=reset_table, width=7)
button_reset.grid(row=8, column=1, padx=5, pady=5, sticky="ew")

window.mainloop()
