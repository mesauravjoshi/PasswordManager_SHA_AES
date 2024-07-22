import string
def validate_input(input_str):
    has_upper = any(char in string.ascii_letters for char in input_str)
    has_lower = any(char in string.ascii_letters for char in input_str)
    has_digit = any(char in string.digits for char in input_str)
    has_punctuation = any(char in string.punctuation for char in input_str)
    if len(input_str) > 6 and has_lower and has_upper and has_digit and has_punctuation:
        return input_str
    else:
        return None

