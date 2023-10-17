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

    def test_id_is_string(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at_assign(self):
        m = BaseModel()
        self.assertTrue(m.created_at)

    def test_updated_at_assign(self):
        m = BaseModel()
        self.assertTrue(m.created_at)

    def assert_updated_at_equal_created_at(self):
        m = BaseModel()
        self.assertEqual(m.created_at, m.updated_at)

    def test_updated_at_changes(self):
        m = BaseModel()
        # store current updated at
        c_updated_at = m.updated_at
        m.save()
        self.assertNotEqual(m.updated_at, c_updated_at)

    def test_save(self):
        m = BaseModel()
        # store current updated at
        c_updated_at = m.updated_at
        m.save()
        self.assertNotEqual(m.updated_at, c_updated_at)

    def test_to_dict(self):
        m = BaseModel()
        m_dict = m.to_dict()
        self.assertEqual(m_dict['__class__'], m.__class__.__name__)
        self.assertEqual(m_dict['created_at'], m.created_at.isoformat())
        self.assertEqual(m_dict['updated_at'], m.updated_at.isoformat())

    def test_str(self):
        m = BaseModel()
        self.assertEqual(m.__str__(), f"[{m.__class__.__name__}] ({m.id}) {m.__dict__}")


if __name__ == "__main__":
    unittest.main()
