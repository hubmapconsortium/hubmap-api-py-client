An iterator provides transparent access the the full result set,
so the user doesn't need to worry about results windowing.

```python
>>> from hubmap_api_py_client.external import ResultsListIterator

>>> class FakeResultsList():
...     def __init__(self, fake_list):
...         self.fake_list = fake_list
...     def __iter__(self):
...         return ResultsListIterator(self.fake_list, window_size=5)
>>> fake = FakeResultsList([])
>>> [f for f in fake]
[]

>>> fake = FakeResultsList(['#0'])
>>> [f for f in fake]
['#0']

>>> fake = FakeResultsList([f'#{n}' for n in range(9)])
>>> [f for f in fake]
['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8']

>>> fake = FakeResultsList([f'#{n}' for n in range(10)])
>>> [f for f in fake]
['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9']

>>> fake = FakeResultsList([f'#{n}' for n in range(11)])
>>> [f for f in fake]
['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10']

```