if __name__ == "__main__":
    line1 = list(map(int, input().split()))
    n = line1[0]
    v = line1[1]
    obj = []
    for i in range(n):
        obj.append(list(map(int, input().split())))
    obj = sorted(obj, key=lambda x: (x[0] / x[1]))
    cost = 0
    while v > 0:
        if obj == []:
            break
        thing = obj.pop()
        if thing[1] >= v:
            cost += v * (thing[0] / thing[1])
            break
        v = v - thing[1]
        cost += thing[0]
    print(f'{cost:.3f}')