def is_anagram(s,t):
    list_s = list(s)
    clone_list_s = list_s
    list_t = list(t)

    for letter in list_t:
        if letter in list_s:
            clone_list_s.remove(letter)
    if len(clone_list_s) == 0 and len(list(s)) == len(list(t)):
        print("they are anagrams")
    else:
        print("they are not anagrams")


is_anagram(input("Enter first word here:"), input("Enter second word here:"))
