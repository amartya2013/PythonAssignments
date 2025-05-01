def replace_character_with_hash(string):
    final_string = string.replace("!", "#").replace("@", "#").replace("$", "#").replace("%", "#").replace("^", "#").replace("&", "#").replace("*", "#").replace("(", "#").replace(")", "#")
    print(final_string)
string = input("Enter your string here:")
replace_character_with_hash(string)