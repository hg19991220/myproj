if __name__ == '__main__':
    #数据源
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
    #创建空的数组
mlist = []
for k in klist:
    #将每个元素都放在ch里
    ch=k
    #去除左右空格
    ch = ch.lstrip()
    ch = ch.rstrip()
    #查看是否存在该列表，如果有的话不添加
    if str(mlist).find(ch)==-1:
        print("出现的字符：",ch,"出现的次数：",str(klist).count(ch))
        mlist.append(ch)
    #显示每个元素出现多少次
    mdict=dict()
for i in mlist:
    mdict[i]=str(klist).count(i)
print(mdict)

