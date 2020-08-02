#!/usr/bin/env python3
from system import open_file

# Exported functions
class UML_markdown():
    pass

# Test functions for module  
def _test():
    _test_UML_markdown_class()

def _test_UML_markdown_class():
    uml_markdown = UML_markdown()

    assert type(uml_markdown) is UML_markdown

if __name__ == '__main__':
    _test()