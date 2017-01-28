class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:

            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

        else:

            new_node = Node(data)
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node


'''

    def insert_at_k(self, data, pos):

        count = 1

        new_node = Node(data)
        temp_node = self.head

        if pos == 1:
            self.head = new_node
            new_node.next = temp_node
        else:
            while (pos != count + 1):
                if temp_node is None:
                    return False
                temp_node = temp_node.next
                count += 1

            new_node.next = temp_node.next
            temp_node.next = new_node

    def insert_atstart(self, data):

        if self.head:
            new_node = Node(data)
            temp_node = self.head
            self.head = new_node
            new_node.next = temp_node
        else:
            new_node = data
            self.head = new_node

        temp_node = self.head
        if data == self.head.data:
            counter = 1

    def print_list(self):

        temp_node = self.head
        while(temp_node):
          print temp_node.data
          temp_node = temp_node.next


    def del_list(self, data):
        temp_node = self.head
        if temp_node is None:
            return None

        if temp_node.data == data:
            # When temp_node is head itself
            self.head = temp_node.next
            temp_node = None
            return True

        while (temp_node.next != None):
            if temp_node.next.data == data:
                next_node = temp_node.next.next
                temp_node.next = None
                temp_node.next = next_node

                return True
            else:
                temp_node = temp_node.next

        return False

'''

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert(0)
    llist.insert(1)
    llist.print_list()
