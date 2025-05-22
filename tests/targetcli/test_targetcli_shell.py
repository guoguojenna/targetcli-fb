import unittest
from unittest.mock import Mock, patch
from targetcli.targetcli_shell import TargetCLI

class TestTargetCLI(unittest.TestCase):
    def setUp(self):
        self.shell = TargetCLI()
    
    def test_shell_initialization(self):
        """Test that shell initializes with correct attributes"""
        self.assertEqual(self.shell.name, "targetcli")
        self.assertIsNotNone(self.shell.prefs)
