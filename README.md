# dict-utils

dict-utils is a set of utilities and accessory methods usable
with Python dicts.

## Examples

1. Search for a value in a dictionary, passing a key:

    ```python
    from dict_utils import dict_utils

    dict_1 = {'first_level': {'second_level': {'name': 'Joe', 'age': 30}}}
    found_value = dict_utils.dict_search_value(dict_1, 'name')
    ```

    **found_value** will contain **'Joe'**

2. Compare two different dictionaries having the same keys

    ```python
    from dict_utils import dict_utils

    dict_1 = {'first_level': {'second_level': {'name': 'Joe', 'age': 30}}}
    dict_2 = {'level_1': {'level_2': {'name': 'Joe', 'age': 30}}}
    dict_utils.compare_assert_dicts(self, ['name', 'age'], dict_1, dict_2)
    ```

## Running Tests

```
python setup.py test
```
