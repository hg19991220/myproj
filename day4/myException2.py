class MyException(Exception):
    def show(self):
        print("异常")
if __name__ == '__main__':
    me=MyException()
    me.show()
    try:
        raise MyException
    except Exception as me:
        print("raise myExcept")
        me.show()