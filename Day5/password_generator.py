import random

numbers = ["1","2","3","4","5","6","7","8","9","0"]
letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h",
           "j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y",
           "U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C",
           "V","B","N","M"]
symbols = [",","?","!",".","_","/","=","#"]
print("Welcome to the PyPassword Generator!")
num_letters =int(input("How many letters would you like in your password?\n"))
num_symbols =int(input("How many symbols would you like in your password?\n"))
num_numbers =int(input("How many numbers would you like in your password?\n"))

# Easy Level
# password = ""
# for char in range(1, num_letters + 1 ):
#     password += random.choice(letters)
# for char in range(1, num_symbols + 1 ):
#     password += random.choice(symbols)
# for char in range(1, num_numbers + 1 ):
#     password += random.choice(numbers)
#
# print(password)

# Hard Level
password_list = []
for char in range(1, num_letters + 1 ):
    password_list.append(random.choice(letters))
for char in range(1, num_symbols + 1 ):
    password_list.append(random.choice(symbols))
for char in range(1, num_numbers + 1 ):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")


