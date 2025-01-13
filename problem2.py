# First we will take a input for the string
string_input = input("Please enter your string with numerals here:")

# Then we will convert the string to a list so it is easier to iterate through
list_input = list(string_input)
clone_list = list(list_input)
# Here we will create a list of all the special characters
number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# Next we will create a counter to keep track of the index of an item in the list
counter = 0
# Now we will iterate through the list
for character in list_input:
    #print(character)
    # We check if the character is a special character
    if character not in number_list:
        # if it is then we change it to a hash

        #print(counter)
        del clone_list[counter]
        #print(clone_list)
        #print(len(clone_list))
        counter -= 1
    # Then we add 1 to counter
    counter += 1
# Then we print the string
final_string = ''
# Now we will print the list by iterating through each character and printing it individually
for letter in clone_list:
    final_string += letter
print(final_string)
print(final_string)