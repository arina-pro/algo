if __name__ == "__main__":
    l1 = list(map(int, input().split()))
    n = l1[0]
    m = l1[1]
    otr = []
    for i in range(n):
        l2 = list(map(int, input().split()))
        otr.append((l2[0], -1, 0))
        otr.append((l2[1], 1, 0))
    points = list(map(int, input().split()))
    for ind, val in enumerate(points):
        otr.append((val, 0, ind))
    otr.sort()
    count = 0
    dots = [0 for j in range(m)]
    for i in otr:
        if i[1] == -1:
            count += 1
        elif i[1] == 0:
            dots[i[2]] = count
        else:
            count -= 1
    for dot in dots:
        print(dot, end=' ')
