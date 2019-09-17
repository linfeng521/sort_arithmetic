class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preTraverse(root):
    if root == None:
        return
    print(root.value, end=' ')
    # 递归
    preTraverse(root.left)
    preTraverse(root.right)


def midTraverse(root):
    '''
    中序遍历
    '''
    if root == None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)


def afterTraverse(root):
    '''
    后序遍历
    '''
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)


if __name__ == '__main__':
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
    preTraverse(root)
