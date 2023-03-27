def colons_in_dialogue(values):
    new_list = []
    for element in values[1:-1]:
        new = element + ": "
        new_list.append(new)
    new_list = [''.join(new_list + list(values[-1]))]
    new_list.insert(0, values[0])
    return new_list

def colons_in_plain_text(values):
    new_list = []
    for element in values[:-1]:
        new = element + ": "
        new_list.append(new)
    new_list = [''.join(new_list + list(values[-1]))]
    return new_list

