def merge(a, b, inv):
    merged = a + b
    a_len = len(a)
    #b_len = len(b)
    a_i = 0
    b_i = a_len
    for i, val in enumerate(merged):
        if merged[a_i] > merged[a_i + b_i]:
            inv += a_len - a_i
            merged[a_i] = merged[a_i + b_i]
            merged.insert(a_i, merged[a_i + b_i])
            a_i += 1
            b_i += 1
        if a == []:
            merged += b
            #[merged.append(i) for i in b]
            break
        elif b == []:
            inv += len(a) - 1
            merged += a
            #[merged.append(i) for i in a]
            break
        elif a[0] > b[0]:
            merged.append(b.pop(0))
            inv += len(a)
        else:
            merged.append(a.pop(0))
    return merged, inv


def merge_sort(n, q):
    inv = 0
    m = list()
    for i in range(n):
        m.append([q[i]])
    length = len(m)
    while length > 1:
        print(m)
        for j in range(length // 2):
                to_m, inv = merge(m[0], m[1], inv)
                print(inv)
                m = m[2:] + [to_m]
        if length % 2 == 1:
            m = m[1:] + [m[0]]
        #    last = m.pop(0)
        #    m.append(last)
        length = len(m)
    return m[0], inv


def read_data_from_txt():
    input = open('inverse_test.txt', 'r')
    n = int(input.readline())
    q = list(map(int, input.readline().split()))
    return n, q


def read_data_from_stdin():
    n = int(input())
    q = list(map(int, input().split()))
    return n, q


if __name__ == "__main__":
    n, q = read_data_from_txt()
    #n, q = read_data_from_stdin()
    print(merge_sort(n, q))