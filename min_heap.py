import numpy as np

class Heap:
    def __init__(self, max_size):
        self.size = 0
        self.heap = np.empty(max_size, dtype=int)
        self.m = []

    def get_parent(self, i):
        if i == 0:
            return None, None
        ind = (i - 1) // 2
        return ind, self.heap[ind]

    def get_left(self, i):
        ind = 2 * i + 1
        if ind > (self.size - 1):
            return None, None
        return ind, self.heap[ind]
    
    def get_right(self, i):
        ind = 2 * i + 2
        if ind > (self.size - 1):
            return None, None
        return ind, self.heap[ind]

    def compare(self, a1, a2):
        return (a1 < a2)
    
    def sift_up(self, i):
        c_val = self.heap[i]
        p_ind, p_val = self.get_parent(i)
        while (i != 0) and (self.compare(c_val, p_val)):
            self.heap[p_ind] = c_val
            self.heap[i] = p_val
            self.m.append([p_ind, i])
            i = p_ind
            c_val = self.heap[i]
            p_ind, p_val = self.get_parent(i)

    def sift_down(self, i):
        p_val = self.heap[i]
        left_ind, left_val = self.get_left(i)
        right_ind, right_val = self.get_right(i)
        #print(left_ind, left_val, right_ind, right_val)
        if (left_val == None) and (right_val == None):
            return 0#break
            #elif (left_val == None):
            #    if (self.compare(right_val, p_val)):
            #        self.heap[right_ind] = p_val
            #        self.heap[i] = right_val
            #        i = right_ind
            #    else:
            #        break
        elif (right_val == None):
            if (self.compare(left_val, p_val)):
                self.heap[left_ind] = p_val
                self.heap[i] = left_val
                self.m.append([i, left_ind])
                    #i = left_ind
            else:
                return 0#break
        elif (left_val != None) and (right_val != None) and \
            ((self.compare(right_val, p_val)) or (self.compare(left_val, p_val))):
            dif_left = p_val - left_val
            dif_right = p_val - right_val
            if dif_left > dif_right:
                self.heap[left_ind] = p_val
                self.heap[i] = left_val
                self.m.append([i, left_ind])
                self.sift_down(left_ind)
            else:
                self.heap[right_ind] = p_val
                self.heap[i] = right_val
                self.m.append([i, right_ind])
                self.sift_down(right_ind)
        else:
            return 0#break

    def insert(self, val):
        self.heap[self.size] = val
        #self.sift_up(self.size)
        self.size += 1
    
if __name__ == "__main__":
    n = int(input())
    heap1 = Heap(n)
    elems = list(map(int, input().split()))
    for i in elems:
        heap1.insert(i)
    for i in range((len(heap1.heap) - 1) // 2, -1, -1):
        heap1.sift_down(i)
    #for i in range(len(heap1.heap) - 1, (len(heap1.heap) - 1) // 2, -1):
    #    heap1.sift_up(i)
    print(len(heap1.m))
    if len(heap1.m) != 0:
        for i in heap1.m:
            print(i[0], end=' ')
            print(i[1])
