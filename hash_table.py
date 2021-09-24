class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custum_hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i)) % self.table_size
        return hash_value

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            while node.pointer:
                node = node.pointer
            node.pointer = Node(Data(key, value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_talble[hashed_key]
            if node.pointer is None:
                return node.data
            while node.pointer:
                if key == node.data.key:
                    return node.data.value
                node = node.pointer

            if key == node.data.key:
                return node.data.value
        return None
        if self.hash_table[hash_key] is None:
            self.hash_talbe[hashed_key] = Node
    
    def print_table(self):
        print("{")
        for idx, val in enumerate(self.hash_table):
            if val is not None:
                out = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        out += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )
                        node = node.next_node
                    out += (
                        str(node.data.key) + " : " + str(node.data.value) + " --> None"
                    )
                    print(f"    [{idx}] {out}")
                else:
                    print(f"    [{idx}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{idx}] {val}")
        print("}")
