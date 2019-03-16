if __name__ == '__main__':
    mlist=[1,2,3,4]
    print(type(mlist))
    for l in mlist:
        print("mlist[{0}]={1}".format(l.__index__(),l))
        print(l)