# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
#
# def greet_with (name, location):
#     print(f"Name : {name}")
#     print(f"Location: {location}")
#
#
# greet_with(location= "ankara", name= "ali")
#
# for letter in "TRUE":
#     print(letter)

def calculate_love_score(name_1, name_2):
    first_calculate = 0
    second_calculate = 0

    name = (name_1 + name_2).upper()

    for letter in "TRUE":
        for i in name:
            if letter == i:
                first_calculate += 1


    for letter in "LOVE":
        for i in name:
            if letter == i:
                second_calculate += 1

    print(str(first_calculate) + str(second_calculate))



calculate_love_score("Kanye West", "Kim Kardashian")
