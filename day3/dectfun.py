def mul(**params):
    print(type(params))
    for p in params.items():
        print(p)
if __name__ == '__main__':
   mul(a="good",v="vv")