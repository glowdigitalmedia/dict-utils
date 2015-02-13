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

    def test_dict_search_found_list_multiple_elements(self):
        dict_1 = {'first_level': [{'second_level': {'name_1': 'Jim', 'age': 30}},
                                    {'second_level': {'name_2': 'Joe', 'age': 30}}]}
        found_value = dict_utils.dict_search_value(dict_1, 'name_2')
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

    def test_compare_dicts_different_order_same_values(self):
        dict_1 = {'alternative_images': ['http://url4.com', 'http://url2.com', 'http://url3.com'],
            'body': '5 stars room from 123 NIS', 'description': 'Blandland',
            'title': 'My little Pony', 'caption': 'WWW.PONY.COM', 'image_url': 'http://url1.com',
            'tracking_url': 'http://x.com'}
        dict_2 = {"title": "My little Pony", "description": "Blandland",
            "body": "5 stars room from 123 NIS", "caption": "WWW.PONY.COM",
            "tracking_url": "http://x.com", "image_url": "http://url1.com",
            "alternative_images": ["http://url2.com", "http://url3.com", "http://url4.com"]}
        dict_utils.compare_assert_dicts(self, ['alternative_images'], dict_1, dict_2)
