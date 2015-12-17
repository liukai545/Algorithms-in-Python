# _*_ encoding:utf-8 _*_

"""
查找某点的直接前驱和直接后继
中序遍历下，如过树中所有关键字都不相同，对于某一节点x，小于x的节点中最大的节点为其前驱节点，大于x的节点中最小的节点为其后继节点

"""


class BTNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BTree:
    def __init__(self, root):
        self.root = root

    def insert(self, data):
        self.__insertNode(data, self.root)

    def __insertNode(self, data, btNode):
        """
        递归的插入节点
        :param data: 数值
        :param btNode: 待插入节点的父节点
        :return:
        """

        if (btNode == None):
            btNode = BTNode(data, None, None)
        elif data < btNode.data:  # 新插入的节点只能放在叶子节点
            if (btNode.left == None):
                btNode.left = BTNode(data, None, None)
                return
            self.__insertNode(data, btNode.left)
        elif data > btNode.data:
            if (btNode.right == None):
                btNode.right = BTNode(data, None, None)
                return
            self.__insertNode(data, btNode.right)

    def printBTree(self):
        self.__printBTreeImpl(self.root)

    def __printBTreeImpl(self, btNode):
        """
        中根遍历
        :param btNode:
        :return:
        """
        if btNode == None:
            return
        self.__printBTreeImpl(btNode.left)
        print(btNode.data)
        self.__printBTreeImpl(btNode.right)

    def delete(self, data):
        """
        1， 叶子节点，直接删除，然后将其父节点指向空
        2，只有左子树或只有右子树，直接将其左子树（右子树）设成父节点左子树（右子树）
        3，有两个子节点，删掉该节点后按照中序遍历保持有序进行调整，有两种方法：
            1，将其替换为中序遍历的直接前驱（或直接后继），然后再再删掉它的直接前驱（或直接后继） 再删是递归的
            2，另其左子树为其父节点的左子树（或右子树，依其是父节点的左子树还是右子树而定），然后其右子树设为其左子树的最右节点的右子树
        :param data:
        :return:
        """
        node = self.find(data)
        if (node.left == None and node.right == None):
            parent = self.find_parent(data)
            if (parent.left == node):
                parent.left = None
            else:
                parent.right = None
        elif (node.left == None and node.right != None):
            parent = self.find_parent(data)
            if (parent.left == node):
                parent.left = node.right
            else:
                parent.right = node.right
        elif (node.left != None and node.right == None):
            parent = self.find_parent(data)
            if (parent.left == node):
                parent.left = node.left
            else:
                parent.right = node.left
        else:
            predecessor_data = self.find_predecessor(data).data
            self.delete(predecessor_data)
            node.data = predecessor_data

    def find_predecessor(self, data):
        """
        找到直接前驱
        先判断x是否有左子树，如果有则在left[x]中查找关键字最大的结点，即是x的前驱。
        如果没有左子树，则从x继续向上执行此操作，直到遇到某个结点是（其父节点的右孩子）结点，*其指某节点*
        此时该父节点就是前驱。
        :return:
        """
        current_node = self.find(data)
        if current_node.left != None:
            pass  # 找最大节点
            current_node = current_node.left
            while current_node.right != None:
                current_node = current_node.right
            return current_node
        else:
            while (True):
                parent_node = self.find_parent(data)
                if (parent_node.right == current_node):
                    return parent_node
                else:
                    current_node = parent_node;
                    parent_node = self.find_parent(current_node.data)

    def find(self, data, btNode=None):

        if (btNode == None):
            btNode = self.root
        if data < btNode.data:
            if btNode.left != None:
                return self.find(data, btNode.left)
            else:
                return None
        elif data > btNode.data:
            if btNode.right != None:
                return self.find(data, btNode.right)
            else:
                return None
        else:
            return btNode

    def find_parent(self, data, btNode=None):
        if (btNode == None):
            btNode = self.root
        if (data == self.root.data):
            return None
        if (btNode.left != None and btNode.left.data == data or btNode.right != None and btNode.right.data == data):
            return btNode
        if (btNode.data > data):
            return self.find_parent(data, btNode.left)
        else:
            return self.find_parent(data, btNode.right)


if __name__ == '__main__':
    root = BTNode(2, None, None)
    btree = BTree(root)
    for i in [5, 8, 3, 1, 4, 9, 0, 7, 6]:
        btree.insert(i)

    btree.printBTree()
    print(btree.find(6))
    print(btree.find_parent(6).data)
    print(btree.find_predecessor(4).data, '4的前驱')

    btree.delete(5)
    btree.printBTree()
