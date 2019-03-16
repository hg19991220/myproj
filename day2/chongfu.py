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
    strs=""
    for i in range(0,len(klist)):
        if(klist.count(klist[i])>1):
            if(strs.find(klist[i])==-1):
                strs+=klist[i]
    for i in range(0,len(strs)):
        print("重复过的字符串为",klist[i])

