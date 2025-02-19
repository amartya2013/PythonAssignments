import csv

with open('students.csv', 'r') as students:
    students_dictionaries = csv.DictReader(students)
    all_marks = {}
    total_marks = {}
    highest_marks = {}
    id_to_name = {}
    for dictionary in students_dictionaries:
        all_marks[f"{dictionary.get('Student ID')},{dictionary.get('Subject')}"] = dictionary.get('Marks')
        id_to_name[dictionary.get('Student ID')] = dictionary.get('Student Name')
    to_sum = []
    for key in all_marks:
        student_ID = key.split(',')[0]
        print(student_ID)
        to_sum.append(int(all_marks[key]))
        for checking_key in all_marks:
            if checking_key.startswith(student_ID) and checking_key.split(',')[1] != key.split(',')[1]:
                to_sum.append(int(all_marks[checking_key]))
                print(all_marks[checking_key])
                total_marks[id_to_name.get(student_ID)] = sum(to_sum)
                highest_marks[id_to_name.get(student_ID)] = max(to_sum)

                print(to_sum)
                break

        to_sum = []

        print(to_sum)


    print(total_marks)
    print(highest_marks)


