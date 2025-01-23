
def take_input_and_return_list(string_separated_input):
    return list(string_separated_input.split(','))


def take_input_and_return_tuple(string_separated_input):
    return tuple(string_separated_input.split(','))


input_string = input("Enter comma separated string here:")
print(take_input_and_return_list(input_string), take_input_and_return_tuple(input_string))

