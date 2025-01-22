
def is_anagram(s, t):
    if set(s) == set(t) and len(s) == len(t):
        print("they are anagram")
    else:
        print("they are not anagrams")


is_anagram(input("first string:"), input("second string:"))
