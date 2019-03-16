if __name__ == '__main__':
    mstr="good good study,day day up"
    mindex=mstr.find("good")
    print(mindex)
    k=mstr.find("s")
    print(k)
    a=mstr.find("up")
    print(a)
    mstr="1,2,5,ds,d,10"
    kk=mstr.find("s")
    print(kk)
    mstr = "good good study,day day up"
    mindex=mstr.find("good",1)
    print(mindex)
    mindex = mstr.find("da",5)
    print(mindex)
    mindex = mstr.find("da",17,25)
    print(mindex)