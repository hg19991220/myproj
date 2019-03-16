if __name__ == '__main__':
    while True:
        hehe=input("你叫什么")

        if hehe=='q':
            break
        else:
            print(hehe)
    print("gun")
if __name__ == '__main__':
    while True:
        zz=input("我是谁")
        if zz=='q':
            break
        else:
            print(zz)
    print("结束")
if __name__ == '__main__':
    while True:
        hg=input("叫什么")
        if hg=='q':
            break;
        else:
            print(hg)
    print("结束")
if __name__ == '__main__':
    myarr=[1,2,3,4,5]
    for m in myarr:
        if m==2:
            continue
        print(m)
if __name__ == '__main__':
    mage=input("your age")
    print(type(mage))
    nage=int(mage)
    print(type(nage))
if __name__ == '__main__':
    mstr="u can u up, u can u go"
    print(mstr[::2])
    print(mstr[::-1])
    print(mstr[::-2])
    print(mstr[1:10:1])
    print(mstr[10:1:-1])
    print(mstr[-10:-1])
if __name__ == '__main__':
    name="good"
    age=18
    addr="beijing"
    print(name,age,addr)
    print(name,age,addr,sep="-")
    print(name,age,addr,sep="-",end=" ")
    print("welcome")
if __name__ == '__main__':
    mystr=[1,2,3,4,5,6,7,8,9]
    for i in mystr:
        for j in mystr:
            if j<=i:
                print(mystr[i-1],"*",mystr[j-1],"=",mystr[i-1]*mystr[j-1],"\t",end="")
            else:
                print(end="")
        print()
if __name__ == '__main__':
    print("{0} hehe {0},{1} zz {3}".format("ke","ee","ll","pp","ss"))
    print("your name is {name} and your age is {age}".format(name="张三",age="18"))
if __name__ == '__main__':
    mystr=[1,2,3,4,5,6,7,8,9]
    for m in mystr:
        print(m)
    for i in mystr:
        for j in mystr:
            if j<=i:
                print(mystr[i-1],"*",mystr[j-1],"=",mystr[i-1]*mystr[j-1],"\t",end="")
            else:
                print(end="")
        print()