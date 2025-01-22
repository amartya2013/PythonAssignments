def is_anagram(s,t):
    if len(s) == len(t) and set(s) == set(t):
        print("they are anagrams")
    else:
        print("they are not anagrams")


is_anagram(input("Enter first word here:"), input("Enter second word here:"))
