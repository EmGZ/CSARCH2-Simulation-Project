def hex_to_utf(hex_input, conversion_type):
    try:
        decimal_value = int(hex_input, 16)
        if conversion_type == "Unicode":
            utf_result = hex(decimal_value)[2:].upper()
        elif conversion_type == "Utf-8 to Hex":
            utf_result = hex(decimal_value)[2:].upper()
        elif conversion_type == "Utf-16 to Hex":
            utf_result = hex(decimal_value)[2:].upper()
        elif conversion_type == "Utf-32 to Hex":
            utf_result = hex(decimal_value)[2:].upper()
        return decimal_value, utf_result
    except ValueError:
        return None, None
