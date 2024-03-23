import re

def check_format(input_string):
    # Define the regular expression pattern
    pattern = re.compile(r'^D[0-9A-Fa-f]{3}D[0-9A-Fa-f]{3}$')

    # Check if the input string matches the pattern
    if pattern.match(input_string):
        return True
    else:
        return False

# Test the function
test_string1 = "D123D45d"
test_string2 = "DABCD456"
test_string3 = "D123DXYZ"

print(check_format(test_string1))  # Output: True
print(check_format(test_string2))  # Output: False
print(check_format(test_string3))  # Output: False
