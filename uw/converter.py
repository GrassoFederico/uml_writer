#!/usr/bin/env python3
from system import open_file

# Exported functions
class UML_markdown:
    
    def __init__(self):
        self._code = Code()

class Code:

    def __init__(self):
        self._file_content = "test"

# Test functions for module  
def _test():
    _test_UML_markdown_class()
    _test_Code_class()

def _test_UML_markdown_class():
    uml_markdown = UML_markdown()
    
    assert isinstance(uml_markdown, UML_markdown)
    assert isinstance(uml_markdown._code, Code)

def _test_Code_class():
    code = Code()

    assert isinstance(code, Code)
    assert isinstance(code._file_content, str)

if __name__ == '__main__':
    _test()