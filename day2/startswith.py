if __name__ == '__main__':
    mstr="u can u up ,no uo no die"
    mbool=mstr.startswith("u")
    print(mbool)
    mbool=mstr.startswith("c",2,4)
    print(mbool)
    mbool = mstr.startswith("c",1,5)
    print(mbool)
    mbool=mstr.endswith(",")