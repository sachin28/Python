class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """ Insert a node """
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            temp_node = self.root
            while (temp_node != None):
                if (data > temp_node.data):
                    if temp_node.right is None:
                        temp_node.right = new_node
                        temp_node = temp_node.right
                    temp_node = temp_node.right
                elif (data <= temp_node.data):
                    if (temp_node.left is None):
                        temp_node.left = new_node
                        temp_node = temp_node.left
                    temp_node = temp_node.left

    def min_node(self):
        """ Print min value """
        temp_node = self.root
        while temp_node.left != None:
            temp_node = temp_node.left
        print "minimum node {}".format(temp_node.data)

    def max_node(self):
        """ Print max value """
        temp_node = self.root
        while temp_node.right != None:
            temp_node = temp_node.right
        print "maximum node {}".format(temp_node.data)

    def search(self, value):
        """ search for a node """
        temp = self.root
        found = False
        while (temp != None and found is False):
            if value == temp.data:
                found = True
            elif (value > temp.data):
                temp = temp.right
            elif (value <= temp.data):
                temp = temp.left

        if found:
            print "{} is in the tree".format(value)
        else:
            print "{} is not in the tree".format(value)

    def print_inorder(self, node):
        """ Print tree in-order """
        if node:
            self.print_inorder(node.left)
            print node.data
            self.print_inorder(node.right)

if __name__ == '__main__':
    bt = BinaryTree()
    for data in [5, 4, 2, 3, 9, 7, 10, 6, 8]:
        bt.insert(data)
    bt.print_inorder(bt.root)
    bt.min_node()
    bt.max_node()
    bt.search(2)
    bt.search(10)
    bt.search(0)
    bt.search(5)
