## Ref: Geeks for Geeks

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None

    def inset(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node

        else:
            new_node = Node(value)
            temp_node = self.head
            while (temp_node.next != None):
                temp_node = temp_node.next

            temp_node.next = new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next






if __name__ == '__main__':

    llist = LinkedList()
    for num in range(0, 5):
        llist.inset(value=num)



    llist.printlist()





