def reg(name,pwd,kk=""):
    if kk:
        user={"name":name,"pwd":pwd,"kk":kk}
    else:
        user={"name":name,"pwd":pwd}
    return user
if __name__ == '__main__':
    #u=reg("good","4321",kk="gg")
    u = reg("good","4321")
    print(u)
