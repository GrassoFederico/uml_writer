#!/usr/bin/env python3

# Exported function
def add(a, b):
    return int(a) + int(b)

# Test function for module  
def _test():
    assert add('1', '1') == 2

if __name__ == '__main__':
    _test()