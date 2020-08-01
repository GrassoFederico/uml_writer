#!/usr/bin/env python3

from uw.system import get_parameters

def main():
    directory_path, output_path = get_parameters()
    
    if(directory_path and output_path):
        print("Processo")
        return 0
    else:
        return -1

if __name__ == '__main__':
    main()