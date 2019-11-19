if __name__ == "__main__":
    l1 = list(map(int, input().split()))
    n = l1[0]
    m = l1[1]
    beg = []
    end = []
    for i in range(n):
        l2 = list(map(int, input().split()))
        beg.append(l2[0])
        end.append(l2[1])
    if m == 1:
        point = int(input())
    else:
        points = list(map(int, input().split()))
    beg = sorted(beg, key=lambda x:x)
    end = sorted(end, key=lambda x:x)
    from bisect import bisect_left
    if m == 1:
        n_begs = bisect_left(beg, point)
        n_ends = bisect_left(end, point)
        print(n_begs - n_ends)
    else:
        for i in points:
            n_begs = bisect_left(beg, i)
            n_ends = bisect_left(end, i)
            print(n_begs - n_ends, end=' ')
