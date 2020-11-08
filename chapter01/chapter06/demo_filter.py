

def use_filer(l):
    rest = filter(lambda n : n % 2 == 0,l)
    return  rest

if __name__ == "__main__":
    l = range(0,51)
    rest = use_filer(l)
    print(list(rest))