#!/usr/bin/env python3
import sys

# Exported functions
def get_directory_path():
    try:
        return sys.argv[1]
    except IndexError:
        return "USAGE: uw.exe [directory_path] [output_path]"

# Test functions for module  
def _test():
    assert isinstance( get_directory_path(), str )

if __name__ == '__main__':
    _test()