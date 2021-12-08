n=int(input())
li=[]
for i in range(n):
    if n<=10:
        s=input()
        if len(s)<=100000:
            res_1=int(s,16)
            res_2=oct(res_1)
            li.append(res_2[2:])
for i in li:
    print(i,end='\n')