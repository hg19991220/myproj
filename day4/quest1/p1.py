import random
def checkSex():
    name=input("请输入姓名")
    sex=input("请输入性别")
    if sex=="男" or sex=="man" or sex=="先生":
        print(name,"先生你好")
    else:
        print(name,"女士你好")
def num():
    tlist=[random.randint(1,100) for l in range(10)]
    print("tlist={tlistKey}".format(tlistKey=tlist))
    glist=[random.randint(1,100) for l in range(15)]
    print("glist={glistKey}".format(glistKey=glist))
    gset=set(tlist+glist)
    print("glist U tlist={glistKey}".format(glistKey=glist))
    print()
def user():
    name=input("输入用户姓名")
    email=input("输入邮箱")
    if len(name)>=6:
        if email.count("@")==1:
            print("信息合法")
        else:
            print("信息不合法")
    else:
        print("信息不合法")
def hui():
    mstr=input("请输入一行字符串")
    if mstr.__len__() % 2 == 1:
        nstr = mstr[::-1]
        print(type(nstr))
        if mstr == nstr:
            print("是回文数")
        else:
            print("不是回文数1")
    else:
        print("不是回文数")
if __name__ == '__main__':
    checkSex()
    num()
    user()
    hui()