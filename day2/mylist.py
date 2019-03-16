if __name__ == '__main__':
    mlist=list() #mlist=[]
    llist=[]
    print(type(mlist))
    print(type(llist))
    #使用append在列表尾添加数据
    mlist.append("班长")
    print(mlist)
    #使用insert在列表指定位置添加数据
    mlist.insert(0,"学委")
    print(mlist)
    #如果不指定位置,则删除最后一个位置
    mlist.pop()
    print(mlist)
    #指定位置从列表中删除
    del mlist[0]
    print(mlist)
    mlist.remove("学委")
    print(mlist)
    mlist.remove("学")
    print(mlist)

