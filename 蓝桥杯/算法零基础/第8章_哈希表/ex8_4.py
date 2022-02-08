import hashlib

def hash_create(school: str):
    data = hashlib.md5()
    data.update(school.encode('utf-8'))
    print('Hash Value(16进位) = ', data.hexdigest())


school = input('请输入学校名称: ')
hash_create(school)
