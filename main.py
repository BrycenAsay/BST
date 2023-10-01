from bst import BST
from pair import Pair

def make_tree():
    """constructs a BST using the 'around the world in 80 days' text file"""     
    samp_tree = BST()
    with open('around-the-world-in-80-days-3.txt', 'r') as la_file:
        while 1:
            something = la_file.read(1)
            if not something:
                break
            is_a_char = ord(something)
            if 47 < is_a_char < 58:                 
                samp_tree.add(Pair(something))
            elif 64 < is_a_char < 91:                 
                samp_tree.add(Pair(something))
            elif 96 < is_a_char < 123:                 
                samp_tree.add(Pair(something))
    return samp_tree

def main():
    ''' Program kicks off here.'''
    bst = make_tree()
    bst.remove(Pair('A'))
    print(bst.postorder())

if __name__ == "__main__":
    main()