import unittest
from BST_Tree import Node


class TestTrees(unittest.TestCase):

    def setUp(self):
        self.tree1 = Node(12)
        self.tree1.Insert(self.tree1, 1)
        self.tree1.Insert(self.tree1, 8)

    def tearDown(self):
        print('teardown')

    def test_Insert(self):
        print('insert')
        self.tree1.Insert(self.tree1, 2)
        self.tree1.Insert(self.tree1, 0)
        self.tree1.PrintTree()

    def test_PrintTree(self):
        print('print')
        self.tree1.PrintTree()


if __name__ == '__main__':
    unittest.main()
