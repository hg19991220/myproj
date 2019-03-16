if __name__ == '__main__':
    mlist=["gun","asd","da asd qwe"]
    mfile=open(r"C:\Users\Hasee\PycharmProjects\myproj\day4.a.c","w")
    mbool=mfile.writable()
    mwr=mfile.write("sdsada")
    print("mwr={mwrkey}".format(mwrkey=mwr))
    mfile.writelines(mlist)
    mfile.close()