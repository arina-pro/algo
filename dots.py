def min_dots(l):
    dot = []
    d = l[0][1]
    dot.append(d)
    for i in l[1:]:
        #print(i)
        #print(i[0])
        if d < i[0]:
            d = i[1]
            #print(d)
            dot.append(d)
    return dot

if __name__ == "__main__":
    #input = open('dots_test.txt', 'r')
    #l = [list(map(int,line.split())) for line in input]
    #l.pop(0)
    
    n = int(input())
    l = []
    for i in range(n):
        a = input()
        a = list(map(int, a.split()))
        print(a)
        l.append(a)
    print(l)
    l = sorted(l, key=lambda x: x[1])
    #print(l[0:])
    dot = min_dots(l)
    print(len(dot))
    [print(i, end=' ') for i in dot]
    