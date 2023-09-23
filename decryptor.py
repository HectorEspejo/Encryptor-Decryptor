from cryptography.fernet import Fernet

filename = input("Select the file you want to decrypt: ")

key = input("Write the key: ")

# Defining the Fernet key for decrypting
f = Fernet(key)

# File chosen by user is opened
with open(filename, "rb") as file:
	encryptedData = file.read()
	

decryptedData = f.decrypt(encryptedData)

with open(filename, "wb") as file:
	file.write(decryptedData)