def edit_distance(s, t):
    d = list()
    l = [0] * (len(t) + 1)
    [d.append(l) for i in range(len(s) + 1)]
    for j in range(len(t) + 1):
        d[0][j] = j
    for i in range(len(s) + 1):
        d[i][0] = i
    d[0][0] = 0
    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            ins = d[i][j - 1] + 1
            rem = d[i - 1][j] + 1
            mat = d[i - 1][j - 1]
            mis = d[i - 1][j - 1] + 1
            #print(s[i], t[j])
            if s[i - 1] == t[j - 1]:
                d[i][j] = min(ins, rem, mat)
            else:
                d[i][j] = min(ins, rem, mis)
    return d[len(s)][len(t)]

def main():
    s = input()
    t = input()
    print(edit_distance(s, t))

if __name__ == "__main__":
    main()