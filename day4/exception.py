def mfun(v):
    if v==0:
        raise Exception("good")
if __name__ == '__main__':
    try:
        mfun(0)
    except Exception as e:
        print("except->{0}".format(e))
        pass
    print("good")