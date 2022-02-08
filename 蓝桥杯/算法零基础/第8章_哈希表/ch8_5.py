import hashlib

data = hashlib.md5()
school = '广州理工学院'
data.update(school.encode('utf-8'))

print('Hash Value         = ', data.digest())
print('Hash Value(16进位) = ', data.hexdigest())
print(type(data))
print(type(data.hexdigest()))