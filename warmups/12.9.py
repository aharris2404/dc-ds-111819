def sum_ages(dict_of_dict):

    sum = 0

    for element in dict_of_dict:
        if element == 'age':
            return dict_of_dict['age']
        elif type(dict_of_dict[element]) is not dict and type(dict_of_dict[element]) is not list:
            continue
        else:
            return sum + sum_ages(dict_of_dict[element])

print(sum_ages({"school_roster": {
    "in_session": "yes",
    "Grade_2": {
        "class_roster": [
            {
            "title": "Teacher",
            "name": "Sierra Vogt",
            "age": 34,
            "height": 182},
            {
            "title": "Student",
            "name": "Blake Cross",
            "age": 12,
            "height": 106},
            {
            "title": "Student",
            "name": "Clint Phlibin",
            "age": 11,
            "height": 120
    }]},
    "Grade_3": {
        "class_roster": [
            {
            "title": "Teacher",
            "name": "Aly Davies",
            "age": 53,
            "height": 162},
            {
            "title": "Student",
            "name": "Alex Heer",
            "age": 13,
            "height": 100},
            {
            "title": "Student",
            "name": "Eric Yost",
            "age": 12,
            "height": 113}
            ]
}}}
))
