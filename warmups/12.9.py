def sum_ages(d):

    sum = 0

    for i, element in enumerate(d):
        
        if element == 'age': #base case
            print('hit base case with age = ' + str(d['age']))
            return d['age']

        if isinstance(d, dict):
            if isinstance(d[element], dict) or isinstance(d[element], list):
                return sum + sum_ages(d[element])
            else:
                continue

        if isinstance(d, list):
            return sum + sum_ages(d[i])

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
