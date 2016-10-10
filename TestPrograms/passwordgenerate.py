import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pswdlen = int(raw_input("number of characters for password: "))
password =  "your password is: " +"".join(random.sample(s,pswdlen ))
print password