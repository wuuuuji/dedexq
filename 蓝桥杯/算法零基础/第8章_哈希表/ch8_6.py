import hashlib

data = hashlib.md5()
filename = 'data8_6.txt'

with open(filename, "rb") as fn:
    btxt = fn.read()
    data.update(btxt)

print('Hash Value         = ', data.digest())
print('Hash Value(16进位) = ', data.hexdigest())
print(type(data))
print(type(data.hexdigest()))