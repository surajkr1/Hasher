
import base64
import uuid

salt = uuid.uuid4().hex
password = input("Enter text to be Hashed : ")
textthashed = password + "  " + salt
hashed_bytes = textthashed.encode('ascii')
base64_bytes = base64.b64encode(hashed_bytes)
base64_bytes2 = base64.b64decode(base64_bytes)


print("Hash (You can share it.) " + str(base64_bytes))
print("You will get your text separated by spaces. \n original text                 hash")
print("Decrypted " + str(base64_bytes2))