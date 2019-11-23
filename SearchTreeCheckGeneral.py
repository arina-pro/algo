class Node():

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def checkNode(self):
        if self.left == None:
            left_v = - (2 ** 31 + 1)
        else:
            left_v = self.left.value
        if self.right == None:
            right_v = 2 ** 31
        else:
            right_v = self.right.value
        if (right_v >= self.value) and (left_v < self.value):
            if self.left:
                self.left.checkNode()
            if self.right:
                self.right.checkNode()
        else:
            return "INCORRECT"

    def createTree(self, i, node_list):
        if node_list[i][1] != -1:
            self.left = Node(node_list[node_list[i][1]][0])
            self.left.createTree(node_list[i][1], node_list)
        if node_list[i][2] != -1:
            self.right = Node(node_list[node_list[i][2]][0])
            self.right.createTree(node_list[i][2], node_list)



class Tree(Node):

    def __init__(self, root=None):
        self.root = root
        self.check = "CORRECT"

    def checkTree(self):
        if self.root:
            self.check = "CORRECT" if self.root.checkNode() == None else "INCORRECT"
        else:
            self.check = "INCORRECT"

    def createTree(self, node_list):
        self.root = Node(node_list[0][0])
        self.root.createTree(0, node_list)



def read_data():
    lines = int(input())
    node_list = list()
    for i in range(lines):
        node_list.append(list(map(int, input().split())))
    return node_list

if __name__ == "__main__":
    node_list = read_data()
    newTree = Tree()
    newTree.createTree(node_list)
    newTree.checkTree()
    print(newTree.check)
