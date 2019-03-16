class MyException(ValueError):
    pass
if __name__ == '__main__':
    try:
        print("before raise exception")
        raise MyException
        print("after raise exception")
    except MyException as me:
        print("catch MyException")
    except ValueError as e:
        print("exception")
        print(e)
    else:
        print("try except else")
    finally:
        print("finally")



    try:
        print("before raise exception")
        raise MyException
        print("after raise exception")
    except MyException as me:
        print("catch MyException")
    except ValueError as e:
        print("exception")
        print(e)
    else:
        print("try except else")
    finally:
        print("finally")