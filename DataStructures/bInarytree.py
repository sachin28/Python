class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
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

    def print_inorder(self, node):
        """ Print tree in-order """
        if node:
            self.print_inorder(node.left)
            print node.data
            self.print_inorder(node.right)

if __name__ == '__main__':
    bt = BinaryTree()
    for data in [5, 4, 2, 3, 1, 9, 7, 10, 6, 8]:
        bt.insert(data)
    bt.print_inorder(bt.root)
