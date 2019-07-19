# Iterative Solution in Traversing a Tree


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_pre_order(root, res):
    # node left right
    if root is not None:
        res.append(root.val)
    if root.left is not None:
        get_pre_order(root.left, res)
    if root.right is not None:
        get_pre_order(root.right, res)


def get_in_order(root, res):
    # left node right
    if root.left is not None:
        get_in_order(root.left, res)

    if root is not None:
        res.append(root.val)

    if root.right is not None:
        get_in_order(root.right, res)


def get_post_order(root, res):
    # left right node
    if root.left is not None:
        get_post_order(root.left, res)

    if root.right is not None:
        get_post_order(root.right, res)

    if root is not None:
        res.append(root.val)


def iterative_inorder(root: Node):
    res = list([int])
    lstack = list([])
    inode = root
    while 1:
        if inode is not None:
            lstack.append(inode)
            inode = inode.left
        else:
            if len(lstack) == 0:
                break
            inode = lstack.pop()
            res.append(inode.val)
            inode = inode.right
    print(f'in_order   : {res}')
    return res


def iterative_postorder(root: Node):
    res = list([int])
    lstack = list([])
    inode = root    # iterator
    pnode = None
    while 1:
        if inode is not None:
            lstack.append(inode)
            inode = inode.left
        else:
            if len(lstack) == 0:
                break
            if lstack[-1].right is None or lstack[-1].right == pnode:
                pnode = lstack.pop()
                res.append(pnode.val)
            else:
                inode = lstack[-1].right
    print(f'post_order : {res}')
    return res


def iterative_preorder(root: Node):
    lstack = list([])
    res = list([int])
    inode = root
    while 1:
        if inode is not None:
            res.append(inode.val)       # Process Current Node
            if inode.right is not None: lstack.append(inode.right)  # Push Right Node
            if inode.left is not None: lstack.append(inode.left)    # Push Left Node, process left side during pop
            if len(lstack) == 0: break
            inode = lstack.pop()

    print(f'pre_order  : {res}')
    return res


if __name__ == '__main__':
    # Create Tree
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(15)
    root.left.right = Node(12)
    root.right = Node(-20)
    root.right.right = Node(9)
    root.right.left = Node(0)
    root.right.left.left = Node(16)
    root.right.left.right = Node(18)

    iterative_postorder(root)
    iterative_inorder(root)
    iterative_preorder(root)
