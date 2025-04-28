def keep_numbers_only(s: str):
    final_print = ""
    for character in s:
        if character.isnumeric():
            final_print += character
        else:
            continue
    return final_print


print(keep_numbers_only(input("Enter string here:")))
