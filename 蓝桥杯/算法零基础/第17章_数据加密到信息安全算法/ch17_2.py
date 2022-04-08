abc = 'abcdefghijklmnopqrstuvwxyz'
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(abc, subText))    # 建立字典
print("打印编码字典\n", encry_dict)     # 打印字典

msgTest = input("请输入原始字符串 : ")

cipher = []
for i in msgTest:                       # 执行每个字符加密
    v = encry_dict[i]                   # 加密
    cipher.append(v)                    # 加密结果
ciphertext = ''.join(cipher)            # 将列表转成字符串

print("原始字符串 ", msgTest)
print("加密字符串 ", ciphertext)
