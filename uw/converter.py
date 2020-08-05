#!/usr/bin/env python3
import re
from abc import ABC, abstractmethod
from system import open_file, get_extension

_FILE_FORMAT_NOT_SUPPORTED = "This file format is not supported"

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

    def build_properties(self):
        return self._code.get_properties()

class Code(ABC):

    def __init__(self, file_path: str):
        try:    
            self._file_content = open_file(file_path, 'r').read()
        except AttributeError:
            print( open_file(file_path, 'r') )            

    @abstractmethod
    def get_properties(self) -> list:
        pass

    @abstractmethod
    def get_methods(self) -> list:
        pass
    
    @abstractmethod
    def get_classes(self) -> list:
        pass
    
    @abstractmethod
    def get_class_relations(self) -> list:
        pass

class PHP(Code):

    __properties_regex = '[ ]+([\w ]+)?[ ]+(private|public|protected)[ ]+\$([\w]+)'

    def get_properties(self) -> list:
        return re.findall(self.__properties_regex, self._file_content)

    def get_methods(self) -> list:
        return ["test"]

    def get_classes(self) -> list:
        return ["test"]

    def get_class_relations(self) -> list:
        return ["test"]

class Vue(Code):

    def get_properties(self) -> list:
        return ["test"]

    def get_methods(self) -> list:
        return ["test"]

    def get_classes(self) -> list:
        return ["test"]

    def get_class_relations(self) -> list:
        return ["test"]

# Test functions for module  
def _test():
    _test_UML_markdown_class()
    _test_Code_extended_classes_file_content()
    _test_PHP_UML_markdown_build()

def _test_UML_markdown_class():
    php_uml_markdown = UML_markdown('./test/Accelerator.php')
    vue_uml_markdown = UML_markdown('./test/Index.vue')
    
    assert isinstance(php_uml_markdown, UML_markdown)
    assert isinstance(php_uml_markdown._code, PHP)
    assert isinstance(vue_uml_markdown, UML_markdown)
    assert isinstance(vue_uml_markdown._code, Vue)

def _test_Code_extended_classes_file_content():
    php_uml_markdown = UML_markdown('./test/Accelerator.php')
    vue_uml_markdown = UML_markdown('./test/Index.vue')

    assert isinstance(php_uml_markdown._code._file_content, str)
    assert isinstance(vue_uml_markdown._code._file_content, str)

def _test_PHP_UML_markdown_build():
    php_test_file_properties = [('', 'protected', 'fillable'), ('', 'protected', 'hidden')]
    php_uml_markdown = UML_markdown('./test/Accelerator.php')

    assert php_uml_markdown.build_properties() == php_test_file_properties

if __name__ == '__main__':
    _test()