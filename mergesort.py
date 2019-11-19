def read_data_from_txt(input):
    n = int(input.readline())
    q = list(map(int, input.readline().split()))
    return n, q


def read_data_from_stdin():
    n = int(input())
    q = list(map(int, input().split()))
    return n, q


def merge(a, b):
    global inv
    merged = Queue()
    from_a = 0
    from_b = 0
    for p in range(a.qsize() + b.qsize()):
        if a.empty():
            [merged.put(b.get()) for i in range(b.qsize())]
            break
        elif b.empty():
            inv += a.qsize() - 1
            [merged.put(a.get()) for i in range(a.qsize())]
            break
        else:
            if from_a == 0:
                from_a = a.get()
            if from_b == 0:
                from_b = b.get()
            if from_a > from_b:
                merged.put(from_b)
                inv += a.qsize()
                from_b = 0
            else:
                merged.put(from_a)
                from_a = 0
    return merged


def mergesort(n, q):
    global inv
    inv = 0
    iter = 0
    Q = Queue()
    for i in q:
        I = Queue()
        I.put(i)
        Q.put(I)
    while Q.qsize() > 1:
        length = Q.qsize()
        for j in range(length // 2):
            Q.put(merge(Q.get(), Q.get()))
        if length % 2 == 1:
            last = Q.get()
            Q.put(last)
    mergedQueue = Q.get()
    return mergedQueue.get()


if __name__ == "__main__":
    from queue import Queue
    input = open('inverse_test.txt', 'r')
    n, q = read_data_from_txt(input)
    #n, q = read_data_from_stdin()
    print(mergesort(n, q))
    print(inv)
