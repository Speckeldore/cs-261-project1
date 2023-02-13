class DLNode:
    """
    Doubly Linked List Node class
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value

class DoublyList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with two sentinels
        """
        self.frontsentinel = DLNode(None)
        self.backsentinel = DLNode(None)
        self.frontsentinel.prev = None
        self.frontsentinel.next = self.backsentinel
        self.backsentinel.prev = self.frontsentinel
        self.backsentinel.next = None
        self.size= 0

    def get_at_index(self, index: int) -> object:
        cur = self.frontsentinel
        for i in range(-1,index):
            cur = cur.next
            if cur.value == None:
                print("Out of index, returned head or tail")
                return cur.value
        return cur.value
dl1 = DoublyList

dl1.get_at_index(1)