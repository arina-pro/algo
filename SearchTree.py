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
    def inorder(self, tree):
        if self.left:
            self.left.inorder(tree)
        tree.inorder_list.append(self.value)
        # print(self.value)
        if self.right:
            self.right.inorder(tree)
    def preorder(self, tree):
        tree.preorder_list.append(self.value)
        if self.left:
            self.left.preorder(tree)
        # print(self.value)
        if self.right:
            self.right.preorder(tree)
    def postorder(self, tree):
        if self.left:
            self.left.postorder(tree)
        # print(self.value)
        if self.right:
            self.right.postorder(tree)
        tree.postorder_list.append(self.value)
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
        self.inorder_list = list()
        self.preorder_list = list()
        self.postorder_list = list()
    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)
    def createTree(self, node_list):
        self.root = Node(node_list[0][0])
        self.root.createTree(0, node_list)
    def inorder(self):
        if self.root:
            self.root.inorder(self)
    def preorder(self):
        if self.root:
            self.root.preorder(self)
    def postorder(self):
        if self.root:
            self.root.postorder(self)


def read_data():
    lines = int(input())
    node_list = list()
    for i in range(lines):
        node_list.append(list(map(int, input().split())))
    return node_list

if __name__ == "__main__":
    #myTree = Tree()
    #print(myTree)
    #nodes = [37,24,42,7,32,2,40,120]
    #for node in nodes:
    #    myTree.insert(node)
    #myTree.inorder()
    #print(myTree.inorder_list)
    #node_list = [[0,7,2], [10,-1,-1], [20,-1,6], [30,8,9],[40,3,-1],[50,-1,-1],[60,1,-1],[70,5,4],[80,-1,-1],[90,-1,-1]]
    node_list = read_data()
    newTree = Tree()
    newTree.createTree(node_list)
    newTree.inorder()
    newTree.preorder()
    newTree.postorder()
    [print(i, end=' ') for i in newTree.inorder_list]
    print('\n')
    [print(i, end=' ') for i in newTree.preorder_list]
    print('\n')
    [print(i, end=' ') for i in newTree.postorder_list]
    # for checking
    import sys
    sys.setrecursionlimit(1000000)
    newTree.inorder()
    isCorrect = [newTree.inorder_list[i] < newTree.inorder_list[i + 1] for i in range(len(newTree.inorder_list) - 1)]
    if sum(isCorrect) == len(newTree.inorder_list) - 1:
        print("CORRECT")
    else:
        print("INCORRECT")
    # did not pass test 14 (or 8 -- I forgot), check before createTree length of node_list and print correct if it is <=1
    # after newTree = Tree() use this code
    if len(node_list) > 1:
        newTree.createTree(node_list)
        # for checking
        import sys
        sys.setrecursionlimit(1000000)
        newTree.inorder()
        isCorrect = [newTree.inorder_list[i] <= newTree.inorder_list[i + 1] for i in range(len(newTree.inorder_list) - 1)]
        if sum(isCorrect) == len(newTree.inorder_list) - 1:
            print("CORRECT")
        else:
            print("INCORRECT")
    # did not pass test 14 (or 8 -- I forgot), check before createTree length of node_list and print correct if it is <=1
    else:
        print("CORRECT")