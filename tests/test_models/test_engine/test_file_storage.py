#!/usr/bin/python3
""" Module for testing the file storage"""
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage methods """
    def setUp(self):
        """ Test for file storage Set up """
        delete_list = []
        for key in storage.all().keys():
            delete_list.append(key)
        for key in delete_list:
            del storage.all()[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ Test add a new object to __objects """
        new_base = BaseModel()
        new_base.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ Test all method and all __objects is properly returned """
        new_base = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ Test save method """
        new_base = BaseModel()
        new_base.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Test Storage file is successfully loaded to __objects """
        new_base = BaseModel()
        new_base.save()
        storage.reload()
        loaded = None
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new_base.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Test load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ Test that BaseModel save method calls storage save """
        new_base = BaseModel()
        new_base.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Test key is properly formatted """
        new_base = BaseModel()
        _id = new_base.to_dict()['id']
        temp = ''
        new_base.save()
        for key, value in storage.all().items():
            if value is new_base:
                temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_get(self):
        """Test that get properly returns a requested object"""
        storage = FileStorage()
        user = User(name="User1")
        user.save()
        self.assertEqual(user, storage.get("User", user.id))

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_count(self):
        """Test that count properly counts all objects"""
        storage = FileStorage()
        nobjs = len(storage._FileStorage__objects)
        self.assertEqual(nobjs, storage.count())
