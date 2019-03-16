if __name__ == '__main__':
    mlist=[1,2,3,4,4,6,5,3]
    count1=len(mlist);
    print(count1)
    mset=set(mlist)
    count2=len((mset))
    print(count2)
    if count1==count2:
        print("无重复")
    else:
        print("有重复字符")