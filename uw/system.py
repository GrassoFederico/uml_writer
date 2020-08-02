#!/usr/bin/env python3
import sys, os

# Exported functions
def get_parameters() -> tuple:
    try:
        return sys.argv[1], sys.argv[2] # argv[1] -> directory path, argv[2] -> output_path
    except IndexError:
        print("USAGE: uw.exe [directory_path] [output_path]")
        return False, False

def explore_directory_path(directory_path: str) -> list:
    result = []

    for root, directoy_names, file_names in os.walk(directory_path):
        for file_name in file_names:
            result.append( os.path.join(root, file_name) )
    
    return result

# Test functions for module  
def _test():
    assert isinstance(get_parameters(), tuple)

if __name__ == '__main__':
    _test()