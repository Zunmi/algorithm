from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        A.sum = A.item.val
        if A.left:   A.sum += A.left.sum
        if A.right:  A.sum += A.right.sum
        left = -float('inf') 
        right = -float('inf')
        middle = A.item.val
        if A.left:
            left = A.left.max_prefix
            middle += A.left.sum
        if A.right:
            right = middle + A.right.max_prefix
        A.max_prefix = max(left, right, middle)
        if A.max_prefix == left:
            A.max_prefix_key = A.left.max_prefix_key
        elif A.max_prefix == right:
            A.max_prefix_key = A.right.max_prefix_key
        else:
            A.max_prefix_key = A.item.key
        #########################################
        # ADD ANY NEW SUBTREE AUGMENTATION HERE #
        #########################################

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        
        k = self.root.max_prefix_key if self.root else None
        s = self.root.max_prefix if self.root else 0
        ##################
        # YOUR CODE HERE #
        ##################
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    n = len(toppings)
    if n == 0: 
        return None, None, 0
    toppings.sort(key=lambda topping: topping[0])
    for (x,y,t) in toppings:
        B.insert(Key_Val_Item(y,t))
        (Y_temp,T_temp) = B.max_prefix()
        if T_temp > T:
            X, Y, T = x, Y_temp, T_temp
            
    return (X, Y, T)
