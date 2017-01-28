def get_integer(help_text):
    return int(input(help_text))


age = get_integer("Tell me your age: ")
school_year = get_integer("What grade are you in? ")
if age > 15:
    print("You are over the age of 15")
    print("You are in grade " + str(school_year))
