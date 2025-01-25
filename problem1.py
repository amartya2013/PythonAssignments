def check_for_multiple_of_seven_and_not_multiple_of_5(start: int, end: int):
    final_list = [str(number) for number in range(start - 1, end + 1) if number % 7 == 0 and number % 5 != 0]
    return final_list


final_string = ', '.join(check_for_multiple_of_seven_and_not_multiple_of_5(2000, 3200))
print(final_string)