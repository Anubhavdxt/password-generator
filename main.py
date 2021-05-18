#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_char = nr_letters + nr_numbers + nr_symbols
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Method 1
# password = ''
# for x in range(1, nr_char+1):
#   if x <= nr_letters:
#     password += letters[random.randint(0,(len(letters)-1))]
#   elif x <= nr_letters + nr_symbols:
#     password += symbols[random.randint(0,(len(symbols)-1))]
#   elif x <= nr_char:
#     password += numbers[random.randint(0,(len(numbers)-1))]
# print(f"Simple Password is: {password}")

# Method 2 [BETTER]
password = ''
for x in range(1, nr_char+1):
  if x <= nr_letters:
    # random.choice() chooses a random element from a list
    password += random.choice(letters)
  elif x <= nr_letters + nr_symbols:
    password += random.choice(symbols)
  elif x <= nr_char:
    password += random.choice(numbers)
print(f"Simple Password is: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_hard = ''

# Method 1
# for x in range(0, len(password)):
#   random_index = random.randint(0, (len(password)-1))
#   password_hard += password[random_index]

## Below line removes a character from the index (random_index)
#   password = password[:random_index] + password[(random_index+1):]


# Method 2 [BETTER]
password_list = []
for x in range(0, len(password)):
  password_list.append(password[x])
# random.shuffle() shuffles the elements of the list
random.shuffle(password_list)
for char in password_list:
  password_hard += char
print(f"Hard Password is: {password_hard}")