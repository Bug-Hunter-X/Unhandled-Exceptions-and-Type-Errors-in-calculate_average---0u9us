def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    total = sum(numeric_numbers)
    return total / len(numeric_numbers)

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_string = [10, 20, 'thirty', 40, 50]
average_string = calculate_average(my_list_with_string)
print(f"The average of a list with a string is: {average_string}")

my_list_with_mix = [10,20, 30.5, 40,50]
average_mix = calculate_average(my_list_with_mix)
print(f"The average of a list with mix is: {average_mix}") 