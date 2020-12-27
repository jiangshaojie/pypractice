# -*- coding: UTF-8 -*-
from arithmetic.util.TreeNode import TreeNode


class binarytree_traverse:
    traverse_path = []

    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(self.root.left)
            self.preorder(self.root.right)

    def inorder(self, root):
        if root:
            self.inorder(self.root.left)
            self.traverse_path.append(root.val)
            self.inorder(self.root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)
