import unittest
from unittest.mock import Mock

from targetcli.ui_node import UINode


class TestUINode(unittest.TestCase):
    def setUp(self):
        self.mock_parent = Mock()
        self.node = UINode(self.mock_parent, "test_node")

    def test_node_initialization(self):
        """Test that UI node initializes with correct attributes"""
        self.assertEqual(self.node.name, "test_node")
        self.assertIs(self.node.parent_node, self.mock_parent)

    def test_path(self):
        """Test path generation"""
        self.mock_parent.path = "/parent"
        self.assertEqual(self.node.path, "/parent/test_node")
