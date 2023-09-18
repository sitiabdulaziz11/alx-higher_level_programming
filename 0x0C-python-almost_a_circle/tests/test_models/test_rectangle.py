import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle(self):
        self.assertIsInstance(Rectangle(5, 3), Base)
