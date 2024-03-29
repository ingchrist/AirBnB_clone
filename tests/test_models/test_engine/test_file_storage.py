#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import wzqUser
from models.state import wzqState
from models.place import wzqPlace
from models.city import wzqCity
from models.amenity import Amenity
from models.review import wzqReview


class wzqTestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class wzqTestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        wzqbm = BaseModel()
        wzqus = wzqUser()
        wzqst = wzqState()
        wzqpl = wzqPlace()
        wzqcy = wzqCity()
        wzqam = Amenity()
        wzqrv = wzqReview()
        models.storage.new(wzqbm)
        models.storage.new(wzqus)
        models.storage.new(wzqst)
        models.storage.new(wzqpl)
        models.storage.new(wzqcy)
        models.storage.new(wzqam)
        models.storage.new(wzqrv)
        self.assertIn("BaseModel." + wzqbm.id, models.storage.all().keys())
        self.assertIn(wzqbm, models.storage.all().values())
        self.assertIn("User." + wzqus.id, models.storage.all().keys())
        self.assertIn(wzqus, models.storage.all().values())
        self.assertIn("State." + wzqst.id, models.storage.all().keys())
        self.assertIn(wzqst, models.storage.all().values())
        self.assertIn("Place." + wzqpl.id, models.storage.all().keys())
        self.assertIn(wzqpl, models.storage.all().values())
        self.assertIn("City." + wzqcy.id, models.storage.all().keys())
        self.assertIn(wzqcy, models.storage.all().values())
        self.assertIn("Amenity." + wzqam.id, models.storage.all().keys())
        self.assertIn(wzqam, models.storage.all().values())
        self.assertIn("Review." + wzqrv.id, models.storage.all().keys())
        self.assertIn(wzqrv, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        bm = BaseModel()
        us = wzqUser()
        st = wzqState()
        pl = wzqPlace()
        cy = wzqCity()
        am = Amenity()
        rv = wzqReview()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = wzqUser()
        st = wzqState()
        pl = wzqPlace()
        cy = wzqCity()
        am = Amenity()
        rv = wzqReview()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
