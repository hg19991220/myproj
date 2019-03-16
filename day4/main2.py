import day4.quest1.p3 as jj
if __name__ == '__main__':
    mdict={
        1:"[1]输入用户姓名及性别，然后给出下列的提示",
        2:"[2]随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
        3:"[3]注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息",
        4:"[4]从键盘输入一行字符串，判断是否是回文数"
    }
    mfunction={
        1:jj.checkSex,
        2:jj.shu,
        3:jj.user,
        4:jj.hui
    }
    while True:
        for l in mdict.values():
            print(l)
        bh=int(input("请输入功能编号"))
        print(mdict.get(bh))
        mfunction.get(bh)()