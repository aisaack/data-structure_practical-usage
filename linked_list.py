class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def to_list(self):
        out = []
        if self.head is None:
            return out

        node = self.head
        while node:
            out.append(node.data)
            node = node.pointer
        return out

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data['id'] is int(user_id):
                return node.data
            node = node.pointer
            return None

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} ->"
            node = node.pointer
        ll_string += 'None'
        print(ll_string)

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return
        # if self.tail is None:
        #     print('The last Node is None')
        #     node = self.head
        #     while node.pointer:
        #         print('iter', node.data)
        #         node = node.pointer
        #         
        #     node.pointer = Node(data, None)
        #     self.last_ndoe = node.pointer

        # else:
        self.tail.pointer = Node(data, None)
        self.tail = self.tail.pointer

