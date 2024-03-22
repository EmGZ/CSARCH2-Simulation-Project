import tkinter as tk
import textwrap as tw
from tkinter import ttk, filedialog, messagebox

def hex_to_utf(utf_input):
    try:
        decimal_value = int(utf_input, 16)
   
        utf_result = []
        utf8 = chr(decimal_value).encode('utf-8').hex().upper()
        utf16 = chr(decimal_value).encode('utf-16be').hex().upper()
        utf32 = chr(decimal_value).encode('utf-32be').hex().upper()
        utf_result.append(' '.join(tw.wrap(utf8, 2)))  # UTF-8
        utf_result.append(' '.join(tw.wrap(utf16, 2)))  # UTF-16
        utf_result.append(' '.join(tw.wrap(utf32, 2)))  # UTF-32
        
        return utf_result
    
    except ValueError:
        return None

def utf_to_hex(hex_input, conversion_type):
    try:
        if conversion_type == "Utf-8":
            hex_result = hex(ord(bytes.fromhex(hex_input).decode('utf-8'))).upper()
        elif conversion_type == "Utf-16":
            hex_result = hex(ord(bytes.fromhex(hex_input).decode('utf-16be'))).upper()
        elif conversion_type == "Utf-32":
            hex_result = hex(ord(bytes.fromhex(hex_input).decode('utf-32be'))).upper()
        
        return hex_result
    except ValueError:
        return None
def validate_hex_input(text):
    if text == '':
        return False  # Do not allow empty string
    if text.startswith('0x') or text.startswith('0X'):
        text = text[2:]
      
    hex_value = int(text, 16)

    if hex_value <= 0x1FFFFF and all(c.upper() in '0123456789ABCDEF' for c in text) and hex_value <= 0x10FFFF and all(c.upper() in '0123456789ABCDEF' for c in text) and all(c.upper() in '0123456789ABCDEF' for c in text) and len(text) <= 8:
        return True
    else:
        return False  # Invalid encoding specified
    
def validate_utf_input(text):
    if text == '':
        return False  # Do not allow empty string
    return all(c.upper() in '0123456789ABCDEF' for c in text) and len(text) <= 8

def convert_input(inputtype):
    result_text = process_input(inputtype)

def process_input(inputtype):
    input_value = entry_input.get().upper()

    if inputtype == "Hex":
        if validate_hex_input(input_value):
            utf_result = hex_to_utf(input_value)
            if utf_result is not None:
                input_value = "U+" + input_value
                add_to_history(input_value, utf_result)
                entry_input.delete(0, 'end')  # Clear the input field
                return utf_result
            else:
                messagebox.showerror("Error", "can not convert!")
            
        else:
            messagebox.showerror("Error", "Invalid input! Please enter a valid hexadecimal value.")
    else:
        if validate_utf_input(input_value):
            hex_result = utf_to_hex(input_value, conversion_var.get())
            if hex_result is not None:
                add_to_history(input_value, hex_result)
                entry_input.delete(0, 'end')  # Clear the input field
                return hex_result
            else:
                messagebox.showerror("Error", "Invalid UTF input!")
        else:
            messagebox.showerror("Error", "Invalid input! Please enter a valid UTF value.")


def add_to_history(input_value, result):
    history.append((input_value, result))
    update_table()
    update_rbutton()
    # print(history)

def update_table():
    table.delete(*table.get_children())
    table['columns'] = ("Input", "Result")
    table.heading("Input", text="Input")
    table.heading("Result", text="Result")
    for item in history:
        table.insert("", "end", values=item)

def reset_table():
    history.clear() # Clear History
    table.delete(*table.get_children()) # Clear Table
    update_rbutton()
    entry_input.delete(0, 'end')  # Clear the input field


def save_to_file(result_text):
    # print(result_text)
    file_path = "output.txt"
    with open(file_path, "w") as file:
        file.write("Input" + "\t\t\t\t\t\t" + "Result" + "\n")
        for i, j in result_text:
            if isinstance(j, list):
                j = ' | '.join(j)  # Handling Multi-value result (Hex to UTFs)
            file.write(i + "\t\t" + j + "\n")   
    messagebox.showinfo("File Updated", "Result saved to {}".format(file_path))

def enable_button(*args):
    if conversion_var.get() or translation_var.get(): 
        button_translate.config(state="normal") # Enable convert button only if an input type is selected 
    else:
        button_translate.config(state="disabled") 

def update_rbutton():
    if history:
        button_reset.config(state="normal")
        button_save.config(state="normal")
    else:
        button_reset.config(state="disabled")
        button_save.config(state="disabled")

    
history = []

window = tk.Tk()
window.title("UNICODE CONVERTER")

label_title = tk.Label(window, text="UNICODE CONVERTER", font=("Helvetica", 30))
label_title.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

label_group = tk.Label(window, text="GROUP 9: CABUNGCAL, DIAZ, GUILLARTE, NGO, SO", font=("Helvetica", 10))
label_group.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

entry_input = tk.Entry(window, font=("Helvetica", 10)) 
entry_input.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

label_group = tk.Label(window, text="Input Type", font=("Helvetica", 10))
label_group.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Radio buttons for conversion type selection
conversion_var = tk.StringVar()

radio_button = tk.Radiobutton(window, text="Hex", variable=conversion_var, value="Hex")
radio_button.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Radio buttons for translation type selection
translation_var = tk.StringVar()

translation_choices = ["Utf-8", "Utf-16", "Utf-32"]
for i, choice in enumerate(translation_choices):
    radio_button = tk.Radiobutton(window, text=choice, variable=conversion_var, value=choice)
    radio_button.grid(row=5, column=1+i, padx=(15, 10), pady=5, sticky="w")

button_translate = tk.Button(window, text="Convert/Translate", command=lambda: convert_input(conversion_var.get()), width=7, state="disabled") # translate_input
button_translate.grid(row=6, column=0, columnspan=4, padx=3, pady=5, sticky="ew")

table = ttk.Treeview(window, show="headings")
table.grid(row=7, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

button_reset = tk.Button(window, text="Reset", command=reset_table, width=7, state="disabled")
button_reset.grid(row=8, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

button_save = tk.Button(window, text="Save Output to File", command=lambda: save_to_file(history), width=7, state="disabled") # Change this to save to file
button_save.grid(row=9, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

conversion_var.trace_add("write", enable_button) 
translation_var.trace_add("write", enable_button)  

window.mainloop()
