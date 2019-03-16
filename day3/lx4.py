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
        ch=k
        ch=ch.lstrip()
        ch=ch.rstrip()
        if str(mlist).find(ch)==-1:
            print("重复出现的字符",ch,"出现的次数",str(klist).count(ch))
            mlist.append(ch)
        mdict=dict()
    for i in mlist:
        mdict[i]=str(klist).count(i)
    print(mdict)
