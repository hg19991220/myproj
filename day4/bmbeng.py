if __name__ == '__main__':
    print("输入两个数,计算除法")
    print("输入q退出")
    while True:
        print("\t")
        fnum=input("First number")
        if fnum=="q":
            break
        snum=input("Second number:")
        if snum=="q":
            break
        try:
            res=int(fnum)/int(snum)
        except ZeroDivisionError as e:
            print("divieion error")
        else:
            print("result={0}".format(res))
        finally:
            pass

        while True:
            print("\t")
            fnum = input("First number")
            if fnum == "q":
                break
            snum = input("Second number:")
            if snum == "q":
                break
            try:
                res = int(fnum) / int(snum)
            except ZeroDivisionError as e:
                print("divieion error")
            else:
                print("result={0}".format(res))
            finally:
                pass