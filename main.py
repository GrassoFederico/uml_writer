#!/usr/bin/env python3

from uw.system import get_parameters, get_directory_file_names

def main():
    directory_path, output_path = get_parameters()
    
    if(directory_path and output_path):
        print('Estraggo i file...')
        file_names = get_directory_file_names(directory_path)
        #print("\n".join(file_names))
        return 0
    else:
        return -1

if __name__ == '__main__':
    main()