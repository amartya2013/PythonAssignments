
def check_for_multiple_of_seven_and_not_multiple_of_5(start: int, end: int):
    final_list = []
    for i in range(start - 1, end + 1):
        if i % 7 == 0 and i % 5 != 0:
            final_list.append(str(i))
        else:
            continue
    return final_list


final_string = ', '.join(check_for_multiple_of_seven_and_not_multiple_of_5(2000, 3200))
print(final_string)
