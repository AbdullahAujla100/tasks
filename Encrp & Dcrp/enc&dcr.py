alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(text, key): 
    cypher = ""

    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + key) % 26
            cypher += alphabets[new_position]
        else:
            cypher += char    

    print(f"Encrypted data is : {cypher}")

def decryption(cypher, key): 
    texty = ""

    for char in cypher:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - key) % 26
            texty += alphabets[new_position]
        else:
            texty += char    

    print(f"Decrypted data is : {texty}")

while True:
    to_do = input("Type Encrypt to do encryption and Decrypt to do decryption and Exit to quit : ").lower()
    
    if to_do == "exit":
        print("GOOD BYE!!")
        break

    elif to_do == "encrypt":
       
        text = input("Enter your word : ").lower()
        key = int(input("Enter your key : "))
        encryption(text, key)
        
    elif to_do == "decrypt":
        text = input("Enter your word : ").lower()
        key = int(input("Enter your key : "))
        decryption(text, key)

    elif to_do not in ["encrypt", "decrypt"]:
        print("Sorry can't understand, type again")
        

