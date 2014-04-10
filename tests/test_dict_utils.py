import unittest

from dict_utils import dict_utils

class DictUtilsTestCase(unittest.TestCase):

    def test_dict_search_found(self):
        dict_1 = {'first_level': {'second_level': {'name': 'Joe', 'age': 30}}}
        found_value = dict_utils.dict_search_value(dict_1, 'name')
        self.assertEqual(found_value, 'Joe', 'Key not found in the given dict')

    def test_dict_search_found_list(self):
        dict_1 = {'first_level': [{'second_level': {'name': 'Joe', 'age': 30}}]}
        found_value = dict_utils.dict_search_value(dict_1, 'name')
        self.assertEqual(found_value, 'Joe', 'Key not found in the given dict')

    def test_dict_search_not_found(self):
        dict_1 = {'first_level': {'second_level': {'name': 'Joe', 'age': 30}}}
        found_value = dict_utils.dict_search_value(dict_1, 'address')
        self.assertNotEquals(found_value, 'London (UK)', 'Key not found in the given dict')

    def test_dict_search_different_value(self):
        dict_1 = {'first_level': {'second_level': {'name': 'Joe', 'age': 30}}}
        found_value = dict_utils.dict_search_value(dict_1, 'name')
        self.assertNotEquals(found_value, 'Paul', 'Found value is not different')

    def test_compare_assert_dicts_identical(self):
        dict_1 = {'first_level': {'second_level': {'name': 'Joe', 'age': 30}}}
        dict_2 = {'first_level': {'second_level': {'name': 'Joe', 'age': 30}}}
        dict_utils.compare_assert_dicts(self, ['name', 'age'], dict_1, dict_2)

    def test_compare_assert_dicts_different_same_values(self):
        dict_1 = {'first_level': {'second_level': {'name': 'Joe', 'age': 30}}}
        dict_2 = {'level_1': {'level_2': {'name': 'Joe', 'age': 30}}}
        dict_utils.compare_assert_dicts(self, ['name', 'age'], dict_1, dict_2)

    def test_compare_assert_dicts_different_keys_structure_same_values(self):
        dict_1 = {'first_level': {'second_level': {'name': 'Joe', 'age': 30}}}
        dict_2 = {'level_1': {'name': 'Joe', 'age': 30}}
        dict_utils.compare_assert_dicts(self, ['name', 'age'], dict_1, dict_2)
