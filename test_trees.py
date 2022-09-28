import unittest
from BST_Tree import Node


class TestTrees(unittest.TestCase):

    def test_Insert(self):

        tree1 = Node(12)
        tree1.Insert(tree1, 1)
        tree1.Insert(tree1, 8)


if __name__ == '__main__':
    unittest.main()
