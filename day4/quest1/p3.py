import random
def checkSex():
    mdict=dict({
        "先生": "先生你好!",
        "男":"先生你好!",
        "man":"先生你好!",
        "Mr.":"先生你好!",
        "boy":"先生你好!",
        "woman":"女士你好!",
        "girl":"女士你好!",
        "Mrs.":"女士你好!",
        "女士":"女士你好"
    })
    name=input("请输入姓名")
    sex=input("请输入性别")
    for l in mdict.keys():
        if l==sex:
            str=l
    print(name,mdict.get(str))
def shu():
    mlist=[random.randint(1,100) for i in range(10)]
    print("mlist={mlistKey}".format(mlistKey=mlist))
    nlist = [random.randint(1, 100) for i in range(15)]
    print("nlist={nlistKey}".format(nlistKey=nlist))
    zset=set(mlist+nlist)
    print("nlist U mlist={zsetKey}".format(zsetKey=zset))
    print()
def user():
    name=input("请输入用户名")
    email=input("输入邮箱")
    if name.__len__() >= 6:
        if email.count("@") == 1:
            mlist = email.split("@")
            print(mlist)
            if mlist.__len__() == 2:
                sun=mlist[0].count(".")
                print(sun)
                if mlist[0].count(".") > 0:
                    print("1不合法")
                else:
                    mylist = mlist[1].split(".")
                    print(mylist)
                    if email.count(".") == 2:
                        if mylist[1] == "com" or mylist[1] == "cn":
                            print("合法")
                    else:
                        print(mylist.__len__())
                        print("2不合法")
            else:
                print("3不合法")
        else:
            print("4不合法")
    else:
        print("5不合法")
def hui():
    chuan=input("请输入一串字符串")
    if chuan.__len__()%2==1:
        if chuan==chuan[::1]:
            print("是回文数")
        else:
            print("不是回文数")
    else:
        print("不是回文数")
if __name__ == '__main__':
    checkSex()
    shu()
    user()
    hui()