import re



m = re.findall(r"([A-Za-z0-9])\1+", raw_input())

print m[0]