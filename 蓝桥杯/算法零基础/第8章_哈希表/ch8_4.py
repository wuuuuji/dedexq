import hashlib

data = hashlib.md5()
data.update(b'Ming-Chi Institute of Technology')

print('Hash Value         = ', data.digest())
print('Hash Value(16进位) = ', data.hexdigest())
print(type(data))
print(type(data.hexdigest()))