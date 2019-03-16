if __name__ == '__main__':
    mstr = input("请输入一行字符串")
    if mstr.__len__()%2==1:
        nstr=mstr[::-1]
        print(type(nstr))
        if mstr == nstr:
            print("是回文数")
        else:
            print("不是回文数1")
    else:
        print("不是回文数")
