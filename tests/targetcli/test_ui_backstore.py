import unittest
from unittest.mock import Mock, patch
from targetcli.ui_backstore import BackstoreNode

class TestBackstoreNode(unittest.TestCase):
    def setUp(self):
        self.mock_parent = Mock()
        self.node = BackstoreNode(self.mock_parent)
    
    def test_backstore_initialization(self):
        """Test that backstore node initializes correctly"""
        self.assertEqual(self.node.name, "backstores")
        self.assertIs(self.node.parent_node, self.mock_parent)
