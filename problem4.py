def is_anagram(s,t):
    list_s = list(s)
    list_t = list(t)

    for i in list_t:
        if i in list_s:
            list_s.remove(i)
        else:
            print("they are not anagrams of each other")
            break
    if len(list_s)== 0:
        print("they are anagrams")

is_anagram('racecar', 'carrace')