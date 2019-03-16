if __name__ == '__main__':
    mfile=open(r"C:\Users\Hasee\PycharmProjects\myproj\day4.a.c")
    #判断当前打开的文件的可读性
    mbool=mfile.readable()
    print(mbool)
    #获取全部文件内容
    val=mfile.read()
    #读取文件的一行
    #返回读取到的内容
    mline=mfile.readline()
    #读取文件所有的行
    #返回一个列表
    mlist=mfile.readlines()
    mfile.close()

    mbool = mfile.readable()
    print(mbool)
    val = mfile.read()
    mline = mfile.readline()
    mlist = mfile.readlines()
    mfile.close()
