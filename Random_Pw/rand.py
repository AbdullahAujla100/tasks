import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
           'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
           'O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['<','!','@','#','$','%','^','&','*','>','?']

n_letters = int(input("Enter the No. of letters you want to add: "))
n_numbers = int(input("Enter the No. of numbers you want to add: "))
n_symbols = int(input("Enter the No. of symbols you want to add: "))

password_list = []
password = ""

for i in range(0, n_letters ):
    char = random.choice(letters)
    password_list += char

for i in range(0, n_numbers):
    char = random.choice(numbers)
    password_list += char

for i in range(0, n_symbols):
    char = random.choice(symbols)
    password_list += char

random.shuffle(password_list)

for i in password_list:
    password += i

print(password)
