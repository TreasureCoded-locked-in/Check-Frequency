def check_frequency(test_dict, value):
    """
    Checks the frequency of a value in a given dictionary.

    Args:
        test_dict: The dictionary to search in.
        value: The value to check the frequency of.

    Returns:
        The number of times the value appears in the dictionary's values, or 0 if 
        the value is not found.
    """
    frequency = 0
    for val in test_dict.values():
        if val == value:
            frequency += 1
    return frequency

# More concise version using count()
def check_frequency_concise(test_dict, value):
    return list(test_dict.values()).count(value)

# Example usage:
test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}

value_to_check = 1
frequency = check_frequency(test_dict, value_to_check)
print(f"The frequency of {value_to_check} is: {frequency}")  # Output: The frequency of 1 is: 3

value_to_check = 4
frequency = check_frequency(test_dict, value_to_check)
print(f"The frequency of {value_to_check} is: {frequency}")  # Output: The frequency of 4 is: 0

frequency_concise = check_frequency_concise(test_dict, 1)
print(f"The frequency of 1 (using concise method) is: {frequency_concise}") # Output: The frequency of 1 (using concise method) is: 3