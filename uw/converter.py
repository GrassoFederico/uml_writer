#!/usr/bin/env python3
from system import open_file

# Exported functions
class UML_markdown:
    
    def __init__(self):
        self._code = Code

class Code:

    pass

# Test functions for module  
def _test():
    _test_UML_markdown_class()

def _test_UML_markdown_class():
    uml_markdown = UML_markdown()

    assert type(uml_markdown) is UML_markdown
    assert uml_markdown._code is Code

if __name__ == '__main__':
    _test()