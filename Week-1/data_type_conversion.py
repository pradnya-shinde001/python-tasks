if __name__ == '__main__':
    # 1. Convert an integer to a floating-point number
    int_var = 10
    float_from_int = float(int_var)
    print(f"Integer {int_var} converted to floating-point: {float_from_int} | Type: {type(float_from_int)}")

    # 2. Convert a floating-point number to an integer
    float_var = 20.5
    int_from_float = int(float_var)
    print(f"Floating-point {float_var} converted to integer: {int_from_float} | Type: {type(int_from_float)}")

    # 3. Convert an integer to a string
    int_var = 42
    string_from_int = str(int_var)
    print(f"Integer {int_var} converted to string: '{string_from_int}' | Type: {type(string_from_int)}")

    # 4. Convert a string containing a number to an integer
    string_var = "100"
    int_from_string = int(string_var)
    print(f"String '{string_var}' converted to integer: {int_from_string} | Type: {type(int_from_string)}")

    # 5. Convert an integer to a Boolean
    int_var = 0  # Try changing this to a non-zero value like 1 or 42
    bool_from_int = bool(int_var)
    print(f"Integer {int_var} converted to Boolean: {bool_from_int} | Type: {type(bool_from_int)}")