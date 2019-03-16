if __name__ == '__main__':
    try:
        mfile=open(r"C:\Users\Hasee\PycharmProjects\myproj\day4")
    except OSError:
        print("oserror")
    except Exception:
        print("Excepetion")
    else:
        mfile.close()
    