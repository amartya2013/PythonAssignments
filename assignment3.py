import csv

with open('students.csv', 'r') as csv_file:
    file_reader = csv.DictReader(csv_file)
    science_marks = {}
    math_marks = {}
    total_marks = {}
    highest_marks = {}
    for dictionary in file_reader:
        if dictionary.get('Subject') == 'Science':
            science_marks[str(dictionary.get('Student Name'))] = str(dictionary.get('Marks'))
        if dictionary.get('Subject') == 'Math':
            math_marks[str(dictionary.get('Student Name'))] = str(dictionary.get('Marks'))
    for key in math_marks.keys():
        total_marks[str(key)] = int(math_marks.get(key)) + int(science_marks.get(key))
        if int(math_marks.get(key)) > int(science_marks.get(key)):
            highest_marks[str(key)] = math_marks.get(key)
        else:
            highest_marks[str(key)] = science_marks.get(key)
    print(highest_marks)
    print(total_marks)
    name = input("Input Me a name:")
    print(f" {name}'s high score is {highest_marks.get(name)} and {name}'s  total score is {total_marks.get(name)}")



