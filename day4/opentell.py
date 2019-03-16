if __name__ == '__main__':
    with open(r"E:\asd.txt",mode="r") as f:
        while True:
            c=f.read(1)
            if c=="":
                break
            print("char=",c)
            print("postion=",f.tell())
            print("*"*30)