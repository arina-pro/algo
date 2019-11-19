def partition(a):
    e = random.choice(a)
    l = []
    lr = []
    r = []
    for i in a:
        if i < e:
            l.append(i)
        elif i == e:
            lr.append(i)
        else:
            r.append(i)
    return l, lr, r


def quicksort(a):
    while len(a) > 1:
        l, lr, r = partition(a)
        return quicksort(l) + lr + quicksort(r)
    return a


if __name__ == "__main__":
    a = '8 3 2 1 5 3 2 4'
    a = list(map(int, a.split()))
    #a = [(0, 1), (1, 2), (0,3), (3, 5), (1, 2)]
    import random
    print(quicksort(a))