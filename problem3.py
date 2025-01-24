import math


def calculate_equation(d: int) -> int:
    return int(math.sqrt((2 * 50 * d) / 30))


input_list = list(input("Give me an input list:").split(','))
final_list = [str(calculate_equation(int(number))) for number in input_list]
print(','.join(final_list))
