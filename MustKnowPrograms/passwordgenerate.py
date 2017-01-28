import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pswdlen = int(raw_input("number of characters for password: "))
pwd = "".join(random.sample(s, pswdlen))
password = "your password is: {} ".format(pwd)
print password
