import string
import time
s1 = string.ascii_letters
s2 = string.digits
s = s1+s2
time_now = time.time()
password = "R64a"
for i1 in range(len(s)):
    s1 = s[i1]
    for i2 in range(len(s)):
        s2 = s[i2]
        for i3 in range(len(s)):
            s3 = s[i3]
            for i4 in range(len(s)):
                s4 = s[i4]
                if s1+s2+s3+s4 == password:
                    print("Я угадал пароль")
                    print(time.time() - time_now)
                    exit(0)
