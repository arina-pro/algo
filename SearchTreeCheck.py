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

    def height(self):
        h = 1
        h = max(h, 1 + (0 if self.left == None else self.left.height()) + (0 if self.right == None else self.right.height()))
        return h

    def checkNode(self):
        if self.left == None:
            left_h = 0
        else:
            left_h = self.left.height()
        if self.right == None:
            right_h = 0
        else:
            right_h = self.right.height()
        if abs(left_h - right_h) > 1:
            return "INCORRECT"
        else:
            if left_h:
                self.left.checkNode()
            if right_h:
                self.right.checkNode()

    def createTree(self, i, node_list):
        if node_list[i][1] != -1:
            self.left = Node(node_list[node_list[i][1]][0])
            self.left.createTree(node_list[i][1], node_list)
        if node_list[i][2] != -1:
            self.right = Node(node_list[node_list[i][2]][0])
            self.right.createTree(node_list[i][2], node_list)

    def createAVL(self, node_list, use_left=False):
        while node_list != list():
            if use_left:
                middle = node_list[len(node_list) // 2 - 1]
            else:
                middle = node_list[len(node_list) // 2 - 1] if len(node_list) % 2 == 0 else node_list[len(node_list) // 2]
            root = Node(middle)
            self.left = createAVL(node_list[:middle], use_left)
            self.right = createAVL(node_list[middle + 1:], use_left)
            return root



class Tree(Node):

    def __init__(self, root=None):
        self.root = root
        self.check = "CORRECT"

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)

    def checkTree(self):
        if self.root:
            self.check = self.root.checkNode()
        else:
            self.check = "INCORRECT"

    def createTree(self, node_list):
        self.root = Node(node_list[0][0])
        self.root.createTree(0, node_list)

    def createAVLTree(self, node_list, use_left=False):
        def createAVL(node_list, use_left):
            if node_list == list():
                return None
            if use_left:
                middle_ind = len(node_list) // 2 - 1
            else:
                middle_ind = len(node_list) // 2 - 1 if len(node_list) % 2 == 0 else len(node_list) // 2
            root = Node(node_list[middle_ind])
            root.left = createAVL(node_list[:middle_ind], use_left)
            root.right = createAVL(node_list[middle_ind + 1:], use_left)
            return root
        self.root = createAVL(node_list, use_left)



def read_data():
    lines = int(input())
    node_list = list()
    for i in range(lines):
        node_list.append(list(map(int, input().split())))
    return node_list

if __name__ == "__main__":
    #node_list = read_data()
    #node_list = [[0,7,2], [10,-1,-1], [20,-1,6], [30,8,9],[40,3,-1],[50,-1,-1],[60,1,-1],[70,5,4],[80,-1,-1],[90,-1,-1]]
    #myTree = Tree()
    #print(myTree)
    #nodes = [6,5,4,3,2,1]
    #for node in nodes:
    #    myTree.insert(node)
    node_list = [-10, -3, 0, 5, 9]
    newTree = Tree()
    newTree.createAVLTree(node_list)
    #newTree.checkTree()
    print(newTree.root)
    print(newTree.root.left)
    print(newTree.root.right)
    print(newTree.root.left.left)#
    print(newTree.root.left.right)
    print(newTree.root.right.left)#
    print(newTree.root.right.right)
