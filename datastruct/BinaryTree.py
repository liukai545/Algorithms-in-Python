# _*_ encoding:utf-8 _*_

"""
一个节点最多有两个孩子节点的树。
对于满二叉树
如果是从0索引开始存储，那么对应于节点p的孩子节点是2p+1和2p+2两个节点，
相反，节点p的父亲节点是(p-1)/2位置上的点
"""

class BinaryTree:
    def __init__(self, root):
        self.key = root;
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node);
            t.left_child = self.left_child
            self.left_child = t;

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


r = BinaryTree('a')

print(r.get_root_val())
print(r.left_child)

r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())


