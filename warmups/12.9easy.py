sum = 0
dictionary_of_dictionary = {} #foo bar here

for roster in dictionary_of_dictionary["school_roster"]:
    if type(dictionary_of_dictionary["school_roster"][roster]) is not dict:
        continue
    else:
        grade_dict_list = dictionary_of_dictionary["school_roster"][roster]["class_roster"]
        for dictionary in grade_dict_list:
            #BONUS: if dictionary["title"] == "Student":
            sum += dictionary["age"]

print(sum)
