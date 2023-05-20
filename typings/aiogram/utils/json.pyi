"""
This type stub file was generated by pyright.
"""

JSON = ...
RAPIDJSON = ...
UJSON = ...
mode = ...
if mode == RAPIDJSON:
    def dump(*args, **kwargs): # -> Any | None:
        ...
    
    def load(*args, **kwargs): # -> Any:
        ...
    
    def dumps(data): # -> Any | str:
        ...
    
    def loads(data): # -> Any:
        ...
    
else:
    def dump(*args, **kwargs): # -> Any | None:
        ...
    
    def load(*args, **kwargs): # -> Any:
        ...
    
    def loads(data): # -> Any:
        ...
    
    def dumps(data): # -> Any | str:
        ...
    
    def dump(*args, **kwargs): # -> Any | None:
        ...
    
    def load(*args, **kwargs): # -> Any:
        ...
    
    def dumps(data): # -> Any | str:
        ...
    
    def loads(data): # -> Any:
        ...
    
