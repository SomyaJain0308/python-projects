"""
Encryption: Instead of storing passwords in plain text, the project uses encryption to protect the stored data.
Master Password: You implement a master password system, which is required to decrypt and view the saved passwords.
Practicality: The project serves as an excellent exercise for learning about basic file handling and security concepts, 
though the creator notes it should be used for educational purposes rather than for storing highly sensitive personal information.
"""
from cryptography.fernet import Fernet
import sys

def gen_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)

def load_key():
    with open("secret.key", "rb") as f:
        return f.read()

def master_key():
    passwo=input("Password: ")
    if passwo=="file@123":
        ask_read_or_add()
    else:
        sys.exit("Wrong Password")        

def ask_read_or_add():
    while True:
        ask=input("Do you want to Read a Password or Add a Password? ").lower().strip()
        if ask=="read":
            read()
            break
        elif ask=="add":
            add()
            break
        else:
            print("Please Enter 'Read' or 'Add'.")
            continue

def read():
    fernet = Fernet(load_key())
    with open("pass.txt") as file:
        lines = file.readlines()    
        for line in lines:
            if "Password:" in line:
                encrypted = line.strip().split("Password: ")[1].encode()
                decrypted = fernet.decrypt(encrypted).decode()
                print(f"Password: {decrypted}")
            else:
                print(line.strip())

def add():
    fernet = Fernet(load_key())
    username=input("Username: ").strip()
    encrypted_pass = fernet.encrypt(input("Password: ").strip().encode())
    with open("pass.txt", "a") as f:
        f.write(f"\nUsername: {username}\nPassword: {encrypted_pass.decode()}\n~~~")
def main():
    master_key()

if __name__=="__main__":
    main()
