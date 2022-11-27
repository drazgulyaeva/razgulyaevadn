import json

INPUT_FILE = "input.csv"

#TODO реализовать конвертер из csv в json
def csv_to_list_dict(input_file) -> list[dict]:
    line_list = []
    values = []
    line_list_values = []
    new_line = '\n'
    delimiter = ','
    list_ = []
    dict_ = {}
    with open(input_file) as file:
        for line in file:
            line_list.append(line.rsplit())
    for item in line_list:
        if item == line_list[0]:
            line_list_keys = item
            keys_list = item[0].split(delimiter)
        else:
            values.append(item)
    for item in values:
        line_list_value = item
        line_list_values.append(item[0].split(delimiter))

    for item in range(len(line_list)-1):
        line_list_item = line_list_values[item]
        for k in range(len(keys_list)):
            dict_[keys_list[k]] = line_list_item[k]
        list_.append(dict_.copy())

    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
