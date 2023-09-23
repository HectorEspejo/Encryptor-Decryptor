# We use cryptography for encryption and Fernet to handle keys
from cryptography.fernet import Fernet

# Generating key
key = Fernet.generate_key()

f = Fernet(key)

filename = input("Write the path to the file you want to encrypt: ")

print("Your key is ", key)

# Opens the file and does its thing
with open(filename, "rb") as file:
	fileData = file.read()
	encryptedData = f.encrypt(fileData)

# Now it is encrypted
with open(filename, "wb") as file:
	file.write(encryptedData)
