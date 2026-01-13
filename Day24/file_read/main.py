with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# m = modify
# r = read
# a = append and not delete
with open("new_file.txt", mode = "a") as file:
    file.write("\nNew text.")
file.close()