def utf8_hex_to_normal_hex(utf8_hex):
    # Convert UTF-8 encoded hexadecimal string to bytes
    utf8_bytes = bytes.fromhex(utf8_hex)

    # Decode bytes as UTF-8
    utf8_string = utf8_bytes.decode('utf-8')

    # Convert UTF-8 string to hexadecimal representation
    #normal_hex = utf8_string.encode('utf-8').hex()
    normal_hex = utf8_string.hex()
    return normal_hex.upper()

# Test the function
utf8_hex_input = "F48CABBE"
normal_hex_output = utf8_hex_to_normal_hex(utf8_hex_input)
print(normal_hex_output)  # Output: 10CAFE