a= input().upper()
b= list(set(a))
max=0
for i in range(len(b)):
    if a.count(b[i])>max:
        max=a.count(b[i])
        result=b[i]
    elif a.count(b[i])==max:
        result='?'
print(result)
