dic={}
for i in range(0,100):
    name=input("请输入名字:")
    if name=="-1":
        break
    else:
        phonenumber=input("请输入手机号码:")
    dic[name]=phonenumber
for i in range(0,100):
    name=input("请输入查询名字:")
    if name=="xxx":
        break
    else:
        print(name,"的手机号码:",dic.get(name))