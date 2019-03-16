if __name__ == '__main__':
    mstr="good good study,day day up"
    mindex=mstr.index("good",1)
    print(mindex)
    minde = mstr.index("st",6)
    print(minde)
    mindx = mstr.index("da",17)
    print(mindx)
    index = mstr.index("tu",5,15)
    print(index)
    ndex = mstr.index("da",7,20)
    print(ndex)
    dex = mstr.index("up",10,26)
    print(dex)