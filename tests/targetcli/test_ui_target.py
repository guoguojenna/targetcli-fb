import unittest
from unittest.mock import Mock, patch
from targetcli.ui_target import UITarget

class TestUITarget(unittest.TestCase):
    def setUp(self):
        self.mock_parent = Mock()
        self.target = UITarget(self.mock_parent, "test_target", "iscsi")
    
    def test_target_initialization(self):
        """Test that target node initializes with correct attributes"""
        self.assertEqual(self.target.name, "test_target")
        self.assertEqual(self.target.wwn, "test_target")
        self.assertEqual(self.target.fabric, "iscsi")
