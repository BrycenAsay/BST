"""imports the pair function that has both a data and a count associated with it""" 
from pair import Pair
class BST:
    """class for a Binary Search Tree"""
    def __init__(self,root=None):
        """initalizes variables"""
        self.root = root

    def is_empty(self, root=None):
        """returns true if BST is empty and False if it is not"""         
        root = self.root
        if not root:
            return True
        return False

    def add(self, number):
        """adds value in the proper place within the BST"""         
        nani = number
        if self.root is None:
            self.root = nani
            return
        prev = None
        temp = self.root
        while temp is not None:
            if temp.data == number.data:
                temp.count += 1
                return
            if temp.data > number.data:
                prev = temp
                temp = temp.left
            elif temp.data < number.data:
                prev = temp
                temp = temp.right
        if prev.data > number.data:
            prev.left = nani
        elif prev.data < number.data:
            prev.right = nani

    def minvaluenode(self, node):
        """find the minimum value node"""         
        current = node
        while current.left is not None:             
            print(current.left.data)
            current = current.left         
            print(current.data)
        return current

    def remove(self, number, root=None, done=False):
        """removes the value it's respective count from the BST"""         
        if not done:
            root = self.root
            number = number.data
            if root.data == number:
                temp = self.minvaluenode(root.right)                 
                print(temp.data)
                self.root = temp
                root.data = temp.data                 
                print(root.right)
                root.right = self.remove(root, temp, True)
        comp_n = number
        if type(number) is not str:
            if comp_n is not None:
                comp_n = number.data
        comp_r = root
        if type(comp_r) is not str:
            if comp_r is not None:
                comp_r = root.data
        else:
            root = Pair(root)
        if root is None:
            return root
        if comp_n < comp_r:
            root.left = self.remove(number, root.left, True)
        elif comp_n > comp_r:
            root.right = self.remove(number, root.right, True)         
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minvaluenode(root.right)
            root.data = temp.data
            root.right = self.remove(root.right, temp.data, True)         
            return root

    def size(self, root=None, done=False):
        """returns the number of items in the BST"""
        if not done:
            root = self.root
        if root is None:
             return 0
        else:
            return(self.size(root.left, True) + 1 + self.size(root.right, True))

    def height(self, root=None, done=False):
        """Returns the height from the root value to the lowest leaf in the BST"""         
        if not done:
            root = self.root
        if root is None:
            return 0
        leftAns = self.height(root.left, True)
        rightAns = self.height(root.right, True)
        return max(leftAns, rightAns) + 1

    def find(self, val, root=None):
        """returns the value if found within the BST"""         
        root = self.root
        while root != None:
            if root.data == val:
                return root.data
            elif val < root.data:
                root = root.left
            elif val > root.data:                 
                root = root.right         
        raise ValueError
    
    def preorder(self, root=None, lyst=[], done=False):         
        """does a preorder traversal of the BST"""
        if not done:
            root = self.root
            lyst = []
        if root:
            lyst.append(root)
            lost = lyst
            self.preorder(root.left, lost, True)
            self.preorder(root.right, lost, True)
        return lyst

    def inorder(self, root=None, lyst=[], done=False):         
        """does an inorder traversal of the BST"""
        if not done:
            root = self.root
            lyst = []
        if root:
            lost = lyst
            self.inorder(root.left,lost, True)             
            lyst.append(root)
            lost = lyst
            self.inorder(root.right,lost, True)
        return lyst

    def postorder(self, root=None, lyst=[], done=False):         
        """does a postorder traveral of the BST"""
        if not done:
            root = self.root
            lyst = []
        if root:
            lost = lyst
            self.postorder(root.left, lost, True)
            self.postorder(root.right, lost, True)             
            lyst.append(root)
            lost = lyst
        return lyst

    def rebalance(self, root=None, ar=None):
        """rebalances the BST"""
        root = self.root
        arr = ar
        if arr == None:
            arr = self.inorder(root)
        if not arr:
            return None
        mid = len(arr) // 2
        root = BST(arr[mid])
        root.left = self.rebalance(None, arr[:mid])
        root.right = self.rebalance(None, arr[mid+1:])         
        return root