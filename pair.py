"""for a class Pair"""
class Pair:
    """creates a class pair that has an associate data and count value"""     
    left = None
    data = None
    count = None
    right = None
    def __init__(self, data=None, count = 1, right=None, left=None):
        self.data = data
        self.count = count
        self.left = left
        self.right = right