import random
import string
s1 = string.ascii_letters
s2 = string.digits
s3 = string.punctuation
s = s1 + s2
password = ""

for i in range(8):
    symbol = random.choice(s)
    password += symbol
print(password)
