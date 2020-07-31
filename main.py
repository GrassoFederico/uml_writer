#Input: percorso cartella + percorso file di output

#!/usr/bin/env python3

from uw.system import get_directory_path

def main():
    directory_path, output_path = get_directory_path()

if __name__ == '__main__':
    main()

#Process: converte l'alberatura in markup UML
#Process: salva il risultato nel percorso di output