name = "sandeep"


def change_name(name):
    print name  # sandeep
    name = name + "1"
    print name  # sandeep1


def print_name(name):
    print name  # sandeep
    change_name(name)
    print name  # sandeep


elements = [1, 2, 3]


def change_elements(elements):
    print elements  # 1,2,3
    elements.append(4)
    print elements  # 1,2,3,4


def print_elements(elements):
    print elements  # 1,2,3
    change_elements(elements)
    print elements  # 1,2,3,4


print_name(name)
print_elements(elements)
