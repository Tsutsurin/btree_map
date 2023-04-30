from BTrees.OOBTree import OOBTree

class BTree_Class:

    bt = OOBTree()

    @staticmethod
    def add_Node(key, value):
        BTree_Class.bt[key] = value


    @staticmethod
    def print_Tree():
        if BTree_Class.size():
            for pair in BTree_Class.bt.iteritems():
                print(pair)

    @staticmethod
    def size():
        if len(BTree_Class.bt) == 0:
            return False
        else:
            return True

    @staticmethod
    def key_value(key):
        if BTree_Class.size():
                if key in BTree_Class.bt:
                    print(BTree_Class.bt[key])
                else:
                    print("Такого ключа не существует")

    @staticmethod
    def remove_key(key):
        if BTree_Class.size():
            del BTree_Class.bt[key]

    @staticmethod
    def remove_all():
        if BTree_Class.size():
            for i in list(BTree_Class.bt.keys()):
                del BTree_Class.bt[i]
        print("Дерево удаленно")