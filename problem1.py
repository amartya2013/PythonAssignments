# First we will take a input for the string
string_input = input("Please enter your string with special characters here:")

# Then we will convert the string to a list so it is easier to iterate through
list_input = list(string_input)
clone_list = list(list_input)
# Here we will create a list of all the special characters
special_character_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
# Next we will create a counter to keep track of the index of an item in the list
counter = 0
# Now we will iterate through the list
for letter in list_input:
    # We check if the character is a special character
    if letter in special_character_list:
        # if it is then we change it to a hash
        clone_list[counter] = '#'
    # Then we add 1 to counter
    counter += 1
# Then we print the string
final_string = ''
# Now we will print the list by iterating through each character and printing it individually
for letter in clone_list:
    final_string += letter
print(final_string)