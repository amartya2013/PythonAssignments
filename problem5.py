
def find_target(target: str, target_list: list) -> int:
    if target in target_list:
        return target_list.index(target)
    else:
        return -1


input_list = list(input("Enter a comma separated string:").split(','))
input_target = input("Enter your target: ")
print(find_target(input_target, input_list))
