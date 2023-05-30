class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(t: TreeNode) -> list[int] :
    if t == [[]]:
        return []
    if t == []:
        return []
    if t is None:
        return []
    output = []
    if t.left != None:
        left = inorder(t.left)
        output += left
    if type(t.val) is int:
        output.append(t.val)
    if t.right != None:
        right = inorder(t.right)
        output += right
    return output

def inorderHelper(t: TreeNode, arr: list[int]) -> list[int] :
    pass

def inorderIterationMethod(t: TreeNode) -> list[int] :
    queue = [t]
    result = []
    while queue:
        cur = queue.pop(0)
        if cur.left != None:
            queue.append(cur.left)
        result.append(cur.val)
        if cur.right != None:
            queue.append(cur.right)
    return result


    

if __name__ == '__main__':
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    t1 = TreeNode(5, l1, l2)
    print(inorder(t1))
    #print(inorderIterationMethod(t1))
    t2 = TreeNode(6, t1, l3)
    print(inorder(t2))
    l5 = TreeNode([[]])
    l6 = TreeNode([])
    print(inorder(l6))
    print(inorder(l5))
    print(inorder([[]]))
    #print(inorderIterationMethod(t2))