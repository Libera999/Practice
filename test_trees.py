import unittest
from BST_Tree import Node


class TestTrees(unittest.TestCase):

    def setUp():
        self.tree1 = Node(12)

    def tearDown():
        print('teardown')

    def test_Insert(self):
        self.tree1.Insert(self.tree1, 1)
        self.tree1.Insert(self.tree1, 8)

    def test_PrintTree(self):
        tree1.PrintTree()


if __name__ == '__main__':
    unittest.main()
