def decimal_to_binary(decimal):
    if decimal == 0:
        return 0

    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

    return binary

def binary_to_decimal(binary):
    power = 0
    decimal = 0

    for digit in reversed(binary):
        if digit == '1':
            decimal += 2 ** power
        power += 1

    return decimal

while True:
    print("Choose option :")
    print("press 1 to change decimal to binary")
    print("press 2 to change binary to decimal")
    print("press 3 to exit")

    choice = input("\nEnter 1, 2 or 3: ")

    if choice == '1':
        num = int(input("Enter decimal number :"))
        print("Binary:", decimal_to_binary(num))

    elif choice == '2':
        string_num = input("Enter binary number :")
        print("Decimal:", binary_to_decimal(string_num))

    elif choice == '3':
        print("Thank you!!! ")
        break

    else:
        print("Invalid choice Try again!!")
