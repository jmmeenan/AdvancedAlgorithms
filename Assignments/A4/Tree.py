import math

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_average(t: TreeNode) -> list[float]:
#Your code here
    if(t == None):
        return []
    thisLevel = []
    nextLevel = []
    thisLevel.append(t)
    level = []
    output = []
    while len(thisLevel) != 0:
        hold = thisLevel.pop(0)
        level.append(hold.val)
        if hold.left != None:
            nextLevel.append(hold.left)
        if hold.right != None:
            nextLevel.append(hold.right)
        if len(thisLevel) == 0 and len(nextLevel) != 0:
            #print("Level")
            #print(level)
            output.append(sum(level)/len(level))
            for i in nextLevel:
                thisLevel.append(i)
            level.clear()
            nextLevel.clear()
        elif len(thisLevel) == 0:
            #print("Level")
            #print(level)
            output.append(sum(level)/len(level))
            level.clear()
            nextLevel.clear()


    return output

def height(t: TreeNode) -> int:
#Your code here
    if t == None:
        return 0
    if t.left == None and t.right == None:
        return 1
    if t.left == None:
        return 1 + height(t.right)
    if t.right == None:
        return 1 + height(t.left)
    else:
        return max((1 + height(t.left)), (1 + height(t.right)))


def diameter(t: TreeNode) -> int:
#Your code here
    if(t == None):
        return 0
    return 1 + height(t.left) + height(t.right)

def max_element(t: TreeNode) -> int:
#Your code here
    if t == None:
        return 0
    hold = t.val
    if t.left != None:
        holdLeft = max_element(t.left)
        if hold < holdLeft:
            hold = holdLeft
    if t.right != None:
        holdRight = max_element(t.right)
        if hold < holdRight:
            hold = holdRight
    return hold

def preorder(t: TreeNode) -> list[float]:
#Your code here
    if(t == None):
        return None
    stack = []
    output = []
    stack.append(t)
    while len(stack) != 0:
        hold = stack.pop()
        output.append(hold.val)
        if hold.right != None:
            stack.append(hold.right)
        if hold.left != None:
            stack.append(hold.left)
    return output

def postorder(t: TreeNode) -> list[float]:
#Your code here
    if t == None:
        return None
    output = []
    if t.left != None:
        output += postorder(t.left)
    if t.right != None:
        output += postorder(t.right)
    output.append(t.val)

    return output

def is_bst(t: TreeNode) -> bool:
#Your code here
    if t == None:
        return True
    if abs(height(t.left) - height(t.right)) > 1:
        return False
    if t.right != None:
        if t.val > t.right.val:
            return False
    if t.left != None:
        if t.val < t.left.val:
            return False
    if t.left != None and t.right != None:
        return is_bst(t.left) and is_bst(t.right)
    return True


if __name__ == '__main__':
    leaf1 = TreeNode(11)
    leaf2 = TreeNode(10)
    branch1 = TreeNode(2, leaf1, leaf2)
    print(preorder(branch1)) #[2, 11, 10]
    print(postorder(branch1)) #[11, 10, 2]
    print(level_average(branch1)) #[2.0, 10.5]
    print(height(branch1)) # 2
    print(diameter(branch1)) # 3
    print(max_element(branch1)) # 11

    print("Next tree")
    leaf3 = TreeNode(6)
    tree = TreeNode(8, branch1, leaf3) 
    print(preorder(tree)) # [8, 2, 11, 10, 6]
    print(postorder(tree)) # [11, 10, 2, 6, 8]
    print(level_average(tree)) #[8.0, 4.0, 10.5]
    print(height(tree)) # 3
    print(diameter(tree)) # 4
    print(max_element(tree)) #11

    print("BST tests")
    l1 = TreeNode(1)
    l3 = TreeNode(20)
    l4 = TreeNode(4)
    l8 = TreeNode(8)
    l5 = TreeNode(5)
    b1 = TreeNode(2, l1, l3)
    b2 = TreeNode(7, l5, l8)
    b3 = TreeNode(4, b1, b2)
    print(is_bst(b3))
