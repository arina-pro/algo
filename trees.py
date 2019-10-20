def height(t, a, h=0, children=[]):
    
    for i in t:
        if i == a:
            children.append(t.index(i))
            print(i, t.index(i), h)
            
    print(children)
    for child in children:
        h = max(h, height(t, child, h + 1, children))
    children=[]
    return h

if __name__ == "__main__":
    #t = input()
    #t = '-1 0 4 0 3'
    #t = '4 -1 4 1 3'
    t = '9 7 5 5 2 9 9 9 2 -1'
    t = list(map(int, t.split()))
    print(height(t, -1))