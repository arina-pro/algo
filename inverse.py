def merge(a, b, inv):
    merged = []
    for p in range(len(a) + len(b)):
        if a[0] > b[0]:
            merged.append(b.pop(0))
            inv += len(a)
        else:
            merged.append(a.pop(0))
        if a == []:
            merged.append(b.pop(0))
        if b == []:
            merged.append(a.pop(0))
    return merged


def inv_count(n, q):
    inv = 0
    for i in range(n):
        inv += 1
    return inv


def read_data_from_txt(input):
    n = int(input.readline())
    q = list(map(int, input.readline().split()))
    return n, q


def read_data_from_stdin():
    n = int(input())
    q = list(map(int, input().split()))
    return n, q


if __name__ == "__main__":
    input = open('inverse_test.txt', 'r')
    n, q = read_data_from_txt(input)
    #n, q = read_data_from_stdin()
    u = zip()