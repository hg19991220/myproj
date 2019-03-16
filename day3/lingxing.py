def paixu():
    for i in range(0, 110):
        print(str(i).rjust(3), end=" ")
        if i % 10 == 9 and i != 0:
            print()
if __name__ == '__main__':
    paixu()
if __name__ =='__main__':

    for i in range(0, 110):

        if (i%10==9  and i!=0):
            print(str(i).rjust(5))
        else:
            print(str(i).rjust(5), end="")



