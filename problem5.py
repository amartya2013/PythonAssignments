
def find_target(target: int, target_list: list) -> int:
    return ''.join(target_list).find(str(target))


input_list = list(input("Enter a comma separated string:").split(','))
input_target = input("Enter your target: ")
print(find_target(int(input_target), input_list))
