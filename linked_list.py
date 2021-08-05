class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        out = []
        if self.head is None:
            return out

        node = self.head
        while node:
            out.append(node.data)
            node = node.next_node
        return out

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data['id'] is int(user_id):
                return node.data
            node = node.next_node
            return None

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} ->"
            node = node.next_node
        ll_string += 'None'
        print(ll_string)

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)

        # if self.last_node is None:
        #     print('The last Node is None')
        #     node = self.head
        #     while node.next_node:
        #         print('iter', node.data)
        #         node = node.next_node
        #         
        #     node.next_node = Node(data, None)
        #     self.last_ndoe = node.next_node

        # else:
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

