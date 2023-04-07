import re


def cut_string(string):
    start_index = string.find("<<")
    end_index = string.find(">>")
    if start_index != -1 and end_index != -1:
        return string[start_index+2:end_index].strip()
    return ""


def parse(s: str) -> list:
    s = "<<"+cut_string(s)+">>"
    elements = re.findall(r'(?<=\|)\[.*?\]|(?<=\|)[^\[]+', s)
    # извлечение должности
    position = re.search(r'^<<"(.+?)"', s).group(1)

    # разбивка всех элементов на списки
    for i in range(len(elements)):
        if elements[i].startswith('['):
            elements[i] = [x.strip().strip('"') for x in elements[i][1:-1].split(',')]
        else:
            elements[i] = elements[i].strip().strip('"')

    return [position, elements[0], elements[1],
    [elements[2], elements[3],elements[4],elements[5],elements[6],elements[7]]]
