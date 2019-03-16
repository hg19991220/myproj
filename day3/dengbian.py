def sanjiao(num):
    print(num)
if __name__ == '__main__':
    num=input("请输入三角形的高")
    sum = int(num)
    i = 0
    while i <= sum:
        j = 0;
        while j < sum - i:
            print(" ", end="")
            j += 1
        j = 0
        while j < 2 * i - 1:
            print("*", end="")
            j += 1
        i += 1
        print()
    i = sum - 1
    sanjiao(num)