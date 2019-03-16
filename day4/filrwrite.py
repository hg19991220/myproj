if __name__ == '__main__':
    f=open(r"./test.txt","w")
    len=f.write("good good study")
    print(len)
    f.close()
    f = open(r"./test.txt", "w")
    len1 = f.write("good qweq study")
    print(len1)
    f.close()