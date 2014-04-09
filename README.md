# dict-utils

dict-utils is a set of utilities and accessory methods usable
with Python dicts.

## Examples

1. Search for a value in a dictionary, passing a key:

    ```python
    from dict_utils import dict_utils

    dict_1 = dict_1 = {'first_level': {'second_level': {'name': 'Joe', 'Age': 30}}}
    found_value = dict_utils.dict_search_value(dict_1, 'name')
    ```

    *found_value* will contain 'Joe'

2. Include the polls URLconf in your project urls.py like this::

      url(r'^polls/', include('polls.urls')),

## Running Tests

```
python setup.py test
```
