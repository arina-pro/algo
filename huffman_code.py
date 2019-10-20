def insert(H, p, F):
    H[size] = F[p]

def extract_min(H):
    return H.pop()

if __name__ == "__main__":
    #s = str(input())
    s = 'bbccdddda'
    symb = {}
    for char in s:
        if char not in symb.keys():
            symb[char] = 1
        else:
            symb[char] += 1
    #symb_val = list(symb.values())
    #symb_val = sorted(symb_val, reverse=True)
    symb_key = sorted(symb.keys(), key=lambda x:symb[x], reverse=True)
    n = len(symb_key)
    print(symb)
    code = {}
    if len(symb_key) == 1:
        code[symb_key[0]] = 0
    while len(symb_key) != 1:
        i = symb_key.pop()
        j = symb_key.pop()
        code[i] = '0'
        code[j] = '1'
        print(i, j, code[i], code[j])
        symb_key.append(j + i)
        print(symb_key[-1])
        symb[j + i] = symb[i] + symb[j]
        print(symb[j + i])
        if len(i) != 1:
            for a in i:
                code[a] = code[i] + code[a]
            code.pop(i, None)
        if len(j) != 1:
            for a in j:
                code[a] = code[j] + code[a]
            code.pop(j, None)
        symb_key = sorted(symb_key, key=lambda x:symb[x], reverse=True)
    print(symb_key)
    print(code)
    #code = sorted(code.keys(), key=lambda x:x[0])
    encode = ''
    for i in s:
        encode += code[i]
    print(n, len(encode))
    for a, b in code.items():
        if len(a) == 1:
            print(a, ': ', b, sep='')
    print(encode)
