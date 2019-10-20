import numpy as np


class Heap:
    def __init__(self, max_size):
        self.size = 0
        self.heap = np.empty(max_size, dtype=int)

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

    def sift_up(self, i):
        c_val = self.heap[i]
        p_ind, p_val = self.get_parent(i)
        while (i != 0) and (c_val > p_val):
            self.heap[p_ind] = c_val
            self.heap[i] = p_val
            i = p_ind
            c_val = self.heap[i]
            p_ind, p_val = self.get_parent(i)
    
    def sift_down(self, i):
        while (i + 1 != self.size):
            p_val = self.heap[i]
            left_ind, left_val = self.get_left(i)
            right_ind, right_val = self.get_right(i)
            print(left_ind, left_val, right_ind, right_val)
            if (left_val == None) and (right_val == None):
                break
            elif (right_val == None):
                if (self.compare(left_val, p_val)):
                    self.heap[left_ind] = p_val
                    self.heap[i] = left_val
                else:
                    break
            elif (left_val != None) and (right_val != None) and \
                ((self.compare(right_val, p_val)) or (self.compare(left_val, p_val))):
                dif_left = p_val - left_val
                dif_right = p_val - right_val
                if dif_left < dif_right:
                    self.heap[left_ind] = p_val
                    self.heap[i] = left_val
                    self.sift_down(left_ind)
                else:
                    self.heap[right_ind] = p_val
                    self.heap[i] = right_val
                    self.sift_down(right_ind)
            else:
                return 0#break

    def insert(self, val):
        self.heap[self.size] = val
        self.sift_up(self.size)
        self.size += 1
        print(self.heap)

    def extract(self):
        if self.heap[0] != None:
            min = self.heap[0]
        last = self.heap[self.size - 1]
        self.heap[0] = last
        self.size -= 1
        print(self.heap)
        self.sift_down(0)
        print(self.heap)
        return min


if __name__ == "__main__":
    n = int(input())
    heap1 = Heap(n)
    for i in range(11):
        line = input().split()
        if line[0] == 'Insert':
            heap1.insert(int(line[-1]))
        if line[0] == 'ExtractMax':
            print(heap1.extract())