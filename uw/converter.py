#!/usr/bin/env python3
from system import open_file, get_extension

_FILE_FORMAT_NOT_SUPPORTED = "Il formato file indicato non è supportato"

# Exported functions
class UML_markdown:
    
    def __init__(self, file_path: str):
        extension = get_extension(file_path)
        
        if(extension == 'php'):
            self._code = PHP(file_path)
        elif(extension == 'vue'):
            self._code = Vue(file_path)
        else:
            raise Exception(_FILE_FORMAT_NOT_SUPPORTED)

class Code:

    def __init__(self, file_path: str):
        self._file_content = open_file(file_path, 'r').read()

class PHP(Code):
    pass

class Vue(Code):
    pass

# Test functions for module  
def _test():
    _test_UML_markdown_class()
    _test_Code_class()

def _test_UML_markdown_class():
    php_uml_markdown = UML_markdown('C:/wamp64/www/php/landing.baro/app/Accelerator.php')
    vue_uml_markdown = UML_markdown('C:/wamp64/www/php/landing.baro/resources/js/components/Index.vue')
    
    assert isinstance(php_uml_markdown, UML_markdown)
    assert isinstance(php_uml_markdown._code, PHP)
    assert isinstance(vue_uml_markdown, UML_markdown)
    assert isinstance(vue_uml_markdown._code, Vue)

def _test_Code_class():
    code = Code('./main.py')

    assert isinstance(code, Code)
    assert isinstance(code._file_content, str)

if __name__ == '__main__':
    _test()