#!/usr/bin/env python3
import sys, os

_FILE_NOT_FOUND_ERROR = "Attenzione! Il file che stai cercando di aprire non esiste!"

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
        result.extend( _get_absolute_file_path(root, file_names) )
    
    return result

def _get_absolute_file_path(root: str, file_names: list) -> list:
    result = []

    for file_name in file_names:
        result.append( os.path.join(root, file_name) )

    return result

def open_file(file_name: str, mode: str):
    try:
        return open(file_name, mode)
    except FileNotFoundError:
        return _FILE_NOT_FOUND_ERROR

# Test functions for module  
def _test():
    _test_get_parameters()
    _test_get_directory_file_names('.')
    _test_open_file()

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

def _test_open_file():
    test_message = "File di test"
    writing_file_pointer = open_file('./test.txt', 'w')
    invalid_file_pointer = open_file('./invalid_file', 'r')

    writing_file_pointer.write( test_message )
    writing_file_pointer.close()
    
    reading_file_pointer = open_file('./test.txt', 'r')
    content = reading_file_pointer.read()
    reading_file_pointer.close()

    os.remove('test.txt')
    
    assert invalid_file_pointer == _FILE_NOT_FOUND_ERROR
    assert content == test_message

if __name__ == '__main__':
    _test()