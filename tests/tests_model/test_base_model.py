#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
class Test_tools(unittest.TestCase):
    def __init__(self):
        """
        Test initials
        """
        models = BaseModel()
                    
        self.assertIsNotNone(models.id)
        self.assertIsNotNone(models.created_at)
        self.assertIsNotNone(models.updated_at)

    def tes_sav(self):
        """
        Test to sav
        """
        models = BaseModel()

        initial_updated_at = models.updated_at

        current_updated_at = models.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def o_dict(self):
        """
        Test  dict
        """
        models = BaseModel()

        my_model_dict = models.to_dict()
                                  
        self.assertIsInstance(model_dict, dict)
                                              
        self.assertEqual(model_dict["__class__"], 'BaseModel')
        self.assertEqual(model_dict['id'], models.id)
        self.assertEqual(model_dict['created_at'], models.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], models.created_at.isoformat())


    def test_str(self):
        """
        Test str
        """
        models = BaseModel()

        self.assertTrue(str(models).startswith('[BaseModel]'))
                       
        self.assertIn(models.id, str(models))
                                                  
        self.assertIn(str(models.__dict__), str(models))


if __name__ == "__main__":
    unittest.main()
