Help on class ResultsSet in hubmap_api_py_client.external:

hubmap_api_py_client.external.ResultsSet = class ResultsSet(builtins.object)
 |  hubmap_api_py_client.external.ResultsSet(client, handle, input_type=None, output_type=None, query=None)
 |  
 |  Instances of ResultsSet subclasses can be combined with set operators,
 |  and then prepared for evaluation by calling get_list(),
 |  which returns a ResultsList.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, other_set)
 |  
 |  __init__(self, client, handle, input_type=None, output_type=None, query=None)
 |      Do not call the constructor directly:
 |      Instead, use the select_* methods on Client.
 |  
 |  __len__(self)
 |  
 |  __or__(self, other_set)
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  __sub__(self, other_set)
 |  
 |  get_list(self, values_included=[], sort_by=None)
 |      Args:
 |          values_included (list[str])
 |          sort_by (str)
 |      
 |      Returns:
 |          ResultsList
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

