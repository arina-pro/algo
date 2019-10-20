def ind_search(a, k):
    l = 1
    r = len(a)
    while l <= r:
        m = (l + r) // 2
        #print(m)
        if a[m - 1] == k:
            return m
        elif a[m - 1] > k:
            r = m - 1
        else:
            l = m + 1
    return -1

def ind_search_dummy(a, k):
    return -1

def read_data_from_txt(input):
    a = list(map(int, input.readline().split()[1:]))
    k = list(map(int, input.readline().split()[1:]))
    return a, k

def read_data_from_stdin():
    a = list(map(int, input().split()))
    a.pop(0)
    a_out = list(map(int, input().split()))
    a_out.pop(0)
    return a, a_out

if __name__ == "__main__":
    input = open('bin_search_test.txt', 'r')
    a, a_out = read_data_from_txt(input)
    #a, a_out = read_data_from_stdin()
    [print(ind_search(a, a_out[i]), end=' ') for i in range(len(a_out))]