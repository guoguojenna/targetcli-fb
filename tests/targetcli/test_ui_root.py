import unittest
from unittest.mock import Mock

from targetcli.ui_root import UIRoot


class TestUIRoot(unittest.TestCase):
    def setUp(self):
        self.shell = Mock()
        self.root = UIRoot(self.shell)

    def test_root_initialization(self):
        """Test that root node initializes with correct attributes"""
        self.assertEqual(self.root.name, "")
        self.assertIs(self.root.shell, self.shell)
