def height(node):
    global children
    #hs = []
    h = 1
    #print(h)
    for child in children[node]:
        #print(child)
        #if children[child] != []:
            #h = max(h, 1 + height(tree, child, h + 1))
        print('child', child)
        print('h before', h)
        h = max(h, 1 + height(child))
        print('h after', h)
        #else:
        #    hs.append(h + 1)
            #print(hs)
    return h#max(hs)

if __name__ == "__main__":
    #import sys
    #sys.setrecursionlimit(20000)
    #n = input()
    #tree = input()
    tree = '9 7 5 5 2 9 9 9 2 -1'
    #tree = '4 -1 4 1 1'
    tree = list(map(int, tree.split()))
    global children
    children = {}
    for i in range(-1, len(tree) + 1):
        children[i] = []
    [children[tree[ind]].append(ind) for ind in range(len(tree))]
    
    print(height(-1) - 1)