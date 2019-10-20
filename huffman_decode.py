if __name__ == "__main__":
    line = list(map(int, input().split()))
    n_uniq = line[0]
    code_len = line[1]
    code = {}
    for i in range(n_uniq):
        line = list(input().split())
        code[line[1]] = line[0][0]
    line = str(input())
    c = ''
    for i in line:
        c += i
        if c in code.keys():
            print(code[c], sep='', end='')
            c = ''