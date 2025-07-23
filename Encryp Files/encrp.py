from cryptography.fernet import Fernet
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "mycsvdata.txt")

if not os.path.exists("mykey.txt"):
    key=Fernet.generate_key()
    with open("mykey.txt","wb") as mykey:
        mykey.write(key)
else:
    with open("mykey.txt","rb") as mykey:
         key=mykey.read()

f=Fernet(key)

with open(file_path,"rb") as original_data:
    original=original_data.read()

encrypted = f.encrypt(original)

with open("enc_csv","wb") as encrypted_file:
    encrypted_file.write(encrypted)


with open("enc_csv","rb") as encrypted_file:
    encryption= encrypted_file.read()

decrypted=f.decrypt(encryption)

with open("dec_csv","wb") as decrypted_file:
    decrypted_file.write(decrypted)


print("Encryption and decryption completed successfully.")