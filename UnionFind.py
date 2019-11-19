class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]


    def find_not_contract(self, p):
        while self.parent[p] != p:
            p = self.parent[p]
        return self.parent[p]


    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]


    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        if self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = self.parent[root_p]
        else:
            self.parent[root_p] = self.parent[root_q]
            if self.rank[root_p] == self.rank[root_q]:
                self.rank[root_q] += 1


    def is_connected(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        connected_p_q = (root_p == root_q)
        return connected_p_q
    


class MergeTables(UnionFind):
    def __init__(self, n, val):
        self.parent = [i for i in range(n)]
        #self.rank = [1 for i in range(n)]
        self.val = val
        self.max_v = max(val)


    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            print(self.max_v)
            return
        #if self.rank[root_p] > self.rank[root_q]:
        #    self.parent[root_q] = self.parent[root_p]
        #    self.val[root_q] += self.val[root_p]
        #    self.val[root_p] = 0
        #    if self.max_v < self.val[root_q]:
        #        self.max_v = self.val[root_q]
        #else:
        print(self.parent)
        self.parent[root_p] = self.parent[root_q]
        print(self.parent)
        self.val[root_p] += self.val[root_q]
        self.val[root_q] = 0
        if self.max_v < self.val[root_p]:
            self.max_v = self.val[root_p]
            #if self.rank[root_p] == self.rank[root_q]:
                #self.rank[root_q] += 1
        print(self.max_v)



def main():
    input = open('MergeTables_test.txt', 'r')
    nm = list(map(int, input.readline().split()))
    val = list(map(int, input.readline().split()))
    myClass = MergeTables(nm[0], val)
    n_pairs = nm[1]
    for i in range(n_pairs):
        pq = list(map(int, input.readline().split()))
        myClass.union(pq[0] - 1, pq[1] - 1)
        print(myClass.val)
        # print(pq[0], 'and', pq[1], 'were connected. It is', myClass.is_connected(pq[0], pq[1]))
    # print(myClass.rank)


def main1():
    input = open('UnionFind_test.txt', 'r')
    n = int(input.readline())
    myClass = UnionFind(n)
    print(myClass.parent)
    n_pairs = 7
    for i in range(n_pairs):
        pq = list(map(int, input.readline().split()))
        myClass.union(pq[0], pq[1])
        print(myClass.parent)
        print(pq[0], 'and', pq[1], 'were connected. It is', myClass.is_connected(pq[0], pq[1]))
    print(myClass.rank)


if __name__ == "__main__":
    main()