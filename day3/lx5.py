if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    mlist=[]
    for k in klist:
        kong=k
        kong=kong.lstrip()
        kong=kong.rstrip()
        if str(mlist).find(kong)==-1:
            print("重复出现的字符",kong,"出现的次数",str(klist).count(kong))
            mlist.append(kong)
        mdict=dict()
    for i in mlist:
        mdict[i]=str(klist).count(i)
    print(mdict)