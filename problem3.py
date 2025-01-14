sample_dict = {'a': 100, 'b': 210, 'c': 300}


def check_for_200(dictionary):
    list_of_values = dictionary.values()  # Gives a list of all the values in the dictionary
    for i in list_of_values:
        if i == 200:
            print("200 is present in the sample dictionary")
        else:
            continue


check_for_200(sample_dict)
