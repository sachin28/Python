def anyNumber():
    return int(raw_input("Give me a number: "))

age = anyNumber()
school_year = anyNumber()

if age > 16:

    print("\nYou are over the age of 15\n")
    print("You are in grade " + str(school_year))