#!/usr/bin/env python3
import sys

# Exported functions
def get_directory_path() -> tuple:
    try:
        return sys.argv[1], sys.argv[2] #argv[1] -> directory path, argv[2] -> output_path
    except IndexError:
        print("USAGE: uw.exe [directory_path] [output_path]")
        return False, False

# Test functions for module  
def _test():
    assert isinstance(get_directory_path(), tuple)

if __name__ == '__main__':
    _test()