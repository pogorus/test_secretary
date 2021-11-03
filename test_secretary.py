import unittest
from unittest import mock
from secretary import *

class TestSecretary(unittest.TestCase):

    def test_check_document_existance_true(self):
        self.assertEqual(check_document_existance('2207 876234'), True)

    def test_check_document_existance_false(self):
        self.assertEqual(check_document_existance('8888'), False)

    def test_get_doc_owner_name(self):
        with unittest.mock.patch('builtins.input', return_value = '2207 876234'):
            self.assertEqual(get_doc_owner_name(), 'Василий Гупкин')

    def test_get_doc_owner_name_none(self):
        with unittest.mock.patch('builtins.input', return_value = '8888'):
            self.assertEqual(get_doc_owner_name(), None)

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'})

    def test_remove_doc_from_shelf(self):
        remove_doc_from_shelf('2207 876234')
        self.assertEqual('2207 876234' in directories['1'], False)
        append_doc_to_shelf('2207 876234', '1')

    def test_add_new_shelf(self):
        add_new_shelf('test')
        self.assertEqual('test' in directories.keys(), True)

    def test_append_doc_to_shelf(self):
        append_doc_to_shelf('test', '1')
        self.assertEqual('test' in directories['1'], True)
        remove_doc_from_shelf('test')


    def test_delete_doc(self):
        with unittest.mock.patch('builtins.input', return_value='2207 876234'):
            delete_doc()
        self.assertEqual(check_document_existance('2207 876234'), False)
        with unittest.mock.patch('builtins.input', side_effect=['2207 876234', 'passport', 'Василий Гупкин', '1']):
            add_new_doc()

    def test_get_doc_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='2207 876234'):
            self.assertEqual(get_doc_shelf(), '1')

    def test_move_doc_to_shelf(self):
        with unittest.mock.patch('builtins.input', side_effect=['2207 876234', '3']):
            move_doc_to_shelf()
        self.assertEqual('2207 876234' in directories['3'], True)
        with unittest.mock.patch('builtins.input', side_effect=['2207 876234', '1']):
            move_doc_to_shelf()

    def test_add_new_doc(self):
        with unittest.mock.patch('builtins.input', side_effect=['test_number', 'test_type', 'Test Owner', '3']):
            add_new_doc()
        self.assertEqual(check_document_existance('test_number'), True)
        with unittest.mock.patch('builtins.input', return_value = 'test_number'):
            self.assertEqual(get_doc_owner_name(), 'Test Owner')
        self.assertEqual('test_number' in directories['3'], True)
        with unittest.mock.patch('builtins.input', return_value='test_number'):
            delete_doc()