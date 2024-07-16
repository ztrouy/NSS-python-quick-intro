def add_numbers(a, b):
    try:
        result = a + b
        print(f"The result is: {result}")
    except TypeError:
        print("Please provide two integers as arguments when invoking this function.")

# Example usage
add_numbers(5, "10")

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print(f"The value for '{key}' is: {value}")
    except KeyError:
        print("Please provide a valid key when invoking this function.")

# Example usage
get_value(my_dict, "name")
get_value(my_dict, "occupation")