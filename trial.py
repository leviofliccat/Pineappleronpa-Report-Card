data1 = {'(Option)>Option 1': ['dialogue1.1', 'dialogue1.2', 'dialogue1.3'], 
 '(Nested)>Option1.1': ['dialogue1.1.1', 'dialogue1.1.2'], 
 '(Option)>Option 2': ['dialogue2.1', 'dialogue2.2', 'dialogue2.3'], 
 '(Option)>Option 3': ['dialogue3.1'], 
 '(Option)>Option 4': ['dialogue4.1', 'dialogue4.2'], 
 '(Option)>Option 5': ['dialogue5.1'], 
 '(Nested)>Option5.1': ['dialogue5.1.1']
 }

def list_from_dict(data):
    a_list = []

    for key in data:
        a_list.append(key)
        a_list.append(data[key])

    b_list = []

    for item in range(len(a_list)//2):
        if a_list[item][0].startswith("(") == True:
            b_list.append(a_list[item])
            a_list.pop(item)

    return a_list

def b_list_from_dict(data):
    a_list = []

    for key in data:
        a_list.append(key)
        a_list.append(data[key])

    b_list = []

    for item in range(len(a_list)//2):
        if a_list[item][0].startswith("(") == True:
            b_list.append(a_list[item])
            a_list.pop(item)

    return b_list

# print(list_from_dict(data1))

