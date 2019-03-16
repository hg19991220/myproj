def getun(names):
    names.append("gun")
if __name__ == '__main__':
    names=["good","luck","to","me"]
    getun(names[:])
    print(names)
    getun(names)
    print(names)