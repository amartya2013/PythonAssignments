
def find_target(target: int, target_list: list) -> int:
    if target in target_list:
        target_index = target_list.index(target)
    else:
        target_index = -1
    return target_index


input_list = list(input("Enter a comma separated string:").split(','))
input_target = input("Enter your target: ")
print(find_target(int(input_target), input_list))
