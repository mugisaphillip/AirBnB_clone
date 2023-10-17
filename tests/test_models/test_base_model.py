#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Unittests for testing of the BaseModel class."""

    def test_id_assigned(self):
        model = BaseModel()
        self.assertTrue(model.id)

    def test_str(self):
        pass


if __name__ == "__main__":
    unittest.main()
