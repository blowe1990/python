#example of the AES module from pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

string="example data"
byte=string.encode()

key=get_random_bytes(16)
cipher=AES.new(key,AES.MODE_EAX)
encrypt=cipher.encrypt_and_digest(byte)

print(encrypt)
