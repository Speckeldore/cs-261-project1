# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:
import random
from queue_and_stack import Queue, Stack
class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree
    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)
class BST:
    """
    Binary Search Tree class
    """
    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None
        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)
    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"
    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)
    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root
    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.
        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True
    # ------------------------------------------------------------------ #
    def add(self, value: object) -> None:
        """
        TODO: Write your implementation
        """
        cur = self._root
        prev = self._root
        last = None
        if self._root == None:
            self._root = BSTNode(value)
        else:
            while cur is not None:
                if last == 'right':
                    prev = prev.right
                if last == 'left':
                    prev = prev.left
                if value >= cur.value:
                    cur = cur.right
                    last = 'right'
                else:
                    cur = cur.left
                    last = 'left'
            cur = BSTNode(value)
            if last == 'left':
                prev.left = cur
            if last == 'right':
                prev.right = cur

#fdkjas
        pass
    def remove(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        parent = self._root
        node = self._root
        last = None
        '''Should iterate till we get to the node'''
        while node.value != value:
            if last == 'right':
                parent = parent.right
            if last == 'left':
                parent = parent.left
            if value > node.value:
                node = node.right
                last = 'right'
            else:
                node = node.left
                last = 'left'
            if node == None:
                return False


        "node has no children"
        if node.left == None and node.right == None:
            if last == 'left':
                parent.left = None
            if last == 'right':
                parent.right = None
            if last == None:
                self._root = None
            return True


        "node has one child"
        if node.left == None or node.right == None:
            if node.left is not None:
                if last == 'left':
                    parent.left = node.left
                if last == 'right':
                    parent.right = node.left
                if last == None:
                    self._root = self._root.left
                return True
            else:
                if last == 'left':
                    parent.left = node.right
                if last == 'right':
                    parent.right = node.right
                if last == None:
                    self._root = self._root.right
                return True

        "If node has 2 children"
        if node.left is not None and node.right is not None:
            parents = node.right
            snode = node.right
            lasts = 0
            while snode.left is not None:
                if lasts == 1:
                    parents = parents.left
                snode = snode.left
                lasts = 1
            if parents is not snode:
                parents.left = snode.right
            if node.right is not snode:
                snode.right = node.right
            snode.left = node.left
            if last == 'left':
                parent.left = snode
            if last == 'right':
                parent.right = snode
            if last == None:
                self._root = snode
            return True


    # Consider implementing methods that handle different removal scenarios; #
    # you may find that you're able to use some of them in the AVL.          #
    # Remove these comments.                                                 #
    # Remove these method stubs if you decide not to use them.               #
    # Change these methods in any way you'd like.                            #
    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        TODO: Write your implementation
        """
        # remove node that has no subtrees (no left or right nodes)
        pass
    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        TODO: Write your implementation
        """
        # remove node that has a left or right subtree (only)
        pass
    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        TODO: Write your implementation
        """
        # remove node that has two subtrees
        # need to find inorder successor and its parent (make a method!)
        pass
    def contains(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        node = self._root
        while node is not None:
            if node.value == value:
                return True
            if value >= node.value:
                node = node.right
            else:
                node = node.left
        return False
        pass
    def inorder_traversal(self,node = 'start', queue = None) -> Queue:
        """
        TODO: Write your implementation
        """
        if queue == None:
            queue = Queue()
        if node == 'start':
            node = self._root
            if node == None:
                return queue
        if node.left is not None:
            self.inorder_traversal(node.left, queue)
        queue.enqueue(node.value)
        if node.right is not None:
            self.inorder_traversal(node.right, queue)
        return queue
        pass
    def find_min(self) -> object:
        """
        TODO: Write your implementation
        """
        node = self._root
        if self._root == None:
            return None

        while node.left is not None:
            node = node.left

        return node.value

        pass
    def find_max(self) -> object:
        """
        TODO: Write your implementation
        """
        node = self._root
        if self._root == None:
            return None

        while node.right is not None:
            node = node.right

        return node.value
        pass
    def is_empty(self) -> bool:
        """
        TODO: Write your implementation
        """
        if self._root == None:
            return True
        else:
            return False
        pass
    def make_empty(self) -> None:
        """
        TODO: Write your implementation
        """
        self._root = None
        pass
# ------------------- BASIC TESTING -----------------------------------------
if __name__ == '__main__':
    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)
    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)
    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)
    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))
    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())
    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())
    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())
    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())
    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())
    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())
    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())
    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())
    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)