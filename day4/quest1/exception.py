if __name__ == '__main__':
    print("输入两个数计算除法")
    print("输入q退出")
    while True:
        print("\t")
        fnum=input("First number:")
        if fnum=="q":
            break
        snum=input("Second number")
        if snum=="q":
            break
    try:
        res=int(fnum)/int(sum)
    except ZeroDivisionError as e:
        pass
    else:
        print("result={0}".format(res))
    finally:
        pass
