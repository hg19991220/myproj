if __name__ == '__main__':
    mstr=[1,2,3,4,5,6,7,8,9]
    for i in mstr:
        for j in mstr:
            print(str(i)+"*"+str(j)+"="+(str(i*j)).rjust(2),end=" ")
            if i==j:
                print()
                break
