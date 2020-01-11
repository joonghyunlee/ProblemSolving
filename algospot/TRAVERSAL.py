import sys


def rl():
    return sys.stdin.readline()


def convert(preorder, inorder, postorder):
    if not preorder:
        return

    root = preorder[0]
    ri = inorder.index(root)

    convert(preorder[1:ri + 1], inorder[:ri], postorder)
    convert(preorder[ri + 1:], inorder[ri + 1:], postorder)

    postorder.append(root)
    return
    

c = int(rl())
n, preorder, inorder, postorder = [], [], [], []
for i in range(c):
    n.append(int(rl()))
    preorder.append(map(int, rl().split()))
    inorder.append(map(int, rl().split()))

    po = []
    convert(preorder[i], inorder[i], po)
    postorder.append(po)

for i in range(c):
    print ' '.join(map(str, postorder[i]))
