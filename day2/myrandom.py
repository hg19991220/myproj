import random
if __name__ == '__main__':
    mynum=[3,7,4,2]
    random.shuffle(mynum)
    print(mynum)
    mynum.sort(reverse=True)
    print(mynum)
    mynum.reverse()
    print(mynum)