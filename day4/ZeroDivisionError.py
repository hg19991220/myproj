if __name__ == '__main__':
    try:
        print(5/0)
    except ZeroDivisionError as e:
        pass
        print("ZeroDivisionError")
        print(e)
    print("good")
