def mul(*params):
    print(type(params))
    for p in params:
        print(p)

if __name__ == '__main__':
    mul("good","luck","to","me")