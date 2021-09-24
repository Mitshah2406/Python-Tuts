#Hashing is a method to generate random values relating to password
#salt is added to hashed password to make it strong so no one can crack it anyway
#this hased password with salt can never be regenerated to normal form
import bcrypt

password = b"MitShah"
hashed = bcrypt.hashpw(password,bcrypt.gensalt())
print(hashed)
passw = input('Enter password: ')
passw = bytes(passw,encoding='utf-8')

if bcrypt.checkpw(passw, hashed):
    print("Login Success")

else:
    print("Invalid password")



