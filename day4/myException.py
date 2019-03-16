#创建一个类
#用来继承来自Exception(所有异常的父类)
#并扩展了一个方法show
class myExcept(Exception):
    def show(self):
        print("达到")
if __name__ == '__main__':
    #创建一个异常
    me=myExcept()
    #使用对象的方法
    me.show()
    try:
        raise myExcept
    except Exception as qw:
        print(" raise myExcept")
        #调用了自定义异常的扩展的方法
        qw.show()