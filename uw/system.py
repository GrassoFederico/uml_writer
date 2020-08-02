#!/usr/bin/env python3
import sys, os

# Exported functions
def get_parameters() -> tuple:
    try:
        return sys.argv[1], sys.argv[2] # argv[1] -> directory path, argv[2] -> output_path
    except IndexError:
        print("USAGE: uw.exe [directory_path] [output_path]")
        return False, False

def get_directory_file_names(directory_path: str) -> list:
    result = []

    for root, directoy_names, file_names in os.walk(directory_path):
        for file_name in file_names:
            result.append( os.path.join(root, file_name) )
    
    return result

# Test functions for module  
def _test():
    _test_get_parameters()
    _test_get_directory_file_names('.')

def _test_get_parameters():
    parameters = get_parameters()

    assert isinstance(parameters, tuple)
    assert isinstance(parameters[0], str)
    assert isinstance(parameters[1], str)

def _test_get_directory_file_names(directory_path: str):
    file_counter = 0

    for root, directoy_names, file_names in os.walk(directory_path):
        for file_name in file_names:
            file_counter += 1

    assert isinstance(get_directory_file_names(directory_path), list)
    assert len(get_directory_file_names(directory_path)) == file_counter

if __name__ == '__main__':
    _test()