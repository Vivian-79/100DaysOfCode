PLACEHOLDER = "[name]"

#make the names to a list
with open("../exercise/Input/names.txt") as names_file:
    names = names_file.readlines()
    # name_replace = name.replace("Aang", "1")
    print(names)

with open("../exercise/Input/email.txt") as letter_file:
    contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode = "w") as completed_letter:
            completed_letter.write(new_letter)



