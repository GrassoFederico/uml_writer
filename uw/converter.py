#!/usr/bin/env python3
import re
from abc import ABC, abstractmethod
from system import open_file, get_extension

_FILE_FORMAT_NOT_SUPPORTED = "This file format is not supported"

# Exported functions
class UML_markdown(ABC):
    
    def __init__(self, file_path: str):
        extension = get_extension(file_path)
        
        if(extension == 'php'):
            self._code = PHP(file_path)
        elif(extension == 'vue'):
            self._code = Vue(file_path)
        else:
            raise Exception(_FILE_FORMAT_NOT_SUPPORTED)

    @abstractmethod
    def build_classes(self):
        pass

    @abstractmethod
    def build_properties(self):
        pass

    @abstractmethod
    def build_methods(self):
        pass

class PlantUML(UML_markdown):

    def build_classes(self):
        return self._code.get_classes()

    def build_properties(self):
        return self._code.get_properties()

    def build_methods(self):
        return self._code.get_methods()


class Code(ABC):

    def __init__(self, file_path: str):
        try:    
            self._file_content = open_file(file_path, 'r').read()
        except AttributeError:
            print( open_file(file_path, 'r') )
    
    @abstractmethod
    def get_namespace(self) -> list:
        pass

    @abstractmethod
    def get_dependencies(self) -> list:
        pass

    @abstractmethod
    def get_classes(self) -> list:
        pass

    @abstractmethod
    def get_properties(self) -> list:
        pass

    @abstractmethod
    def get_methods(self) -> list:
        pass

class PHP(Code):

    __classes_regex = r' *(\w+)? *(class|interface) +(\w+) *(extends|implements)? *(\w+)?'
    __properties_regex = r'[ \t]+([abstract|static| ]+)? *(protected|public|private)? +\$(?![\w]+\->)(\w+)'
    __methods_regex = r' *([abstract|static| ]+)? *(protected|public|private)? *function +(\w+)\(([\\\w \$]*)\)[: ]*([\\\w]*)'

    def get_namespace(self) -> list:
        pass

    def get_dependencies(self) -> list:
        pass

    def get_classes(self) -> list:
        return re.findall(self.__classes_regex, self._file_content)

    def get_properties(self) -> list:
        return re.findall(self.__properties_regex, self._file_content)

    def get_methods(self) -> list:
        return re.findall(self.__methods_regex, self._file_content)

class Vue(Code):

    def get_namespace(self) -> list:
        pass

    def get_dependencies(self) -> list:
        pass

    def get_classes(self) -> list:
        return ["test"]

    def get_properties(self) -> list:
        return ["test"]

    def get_methods(self) -> list:
        return ["test"]

# Test functions for module  
def _test():
    _test_UML_markdown_class()
    _test_Code_extended_classes_file_content()
    _test_PHP_extract_data()

def _test_UML_markdown_class():
    php_uml_markdown = PlantUML('./test/test.php')
    vue_uml_markdown = PlantUML('./test/test.vue')
    
    assert isinstance(php_uml_markdown, UML_markdown)
    assert isinstance(php_uml_markdown._code, PHP)
    assert isinstance(vue_uml_markdown, UML_markdown)
    assert isinstance(vue_uml_markdown._code, Vue)

def _test_Code_extended_classes_file_content():
    php_uml_markdown = PlantUML('./test/test.php')
    vue_uml_markdown = PlantUML('./test/test.vue')

    assert isinstance(php_uml_markdown._code._file_content, str)
    assert isinstance(vue_uml_markdown._code._file_content, str)

def _test_PHP_extract_data():
    php_test_file_classes = [('abstract', 'class', 'Test', '', ''), ('', 'class', 'PaymentController', 'extends', 'Controller')]
    php_test_file_properties = [('', 'private', 'order'), ('', 'private', 'remote_controller'), ('', 'private', 'payment_identifier'), ('', 'private', 'order'), ('', 'private', 'remote_controller'), ('', 'private', 'payment_identifier'), ('', 'private', 'payer_identifier'), ('', '', 'registry'), ('', '', 'result'), ('', '', 'state')]
    php_test_file_methods = [('', 'public', 'create', 'Request $request', ''), ('', 'public', 'return', 'Request $request', ''), ('', 'public', 'execute', 'Request $request', ''), ('', 'public', 'cancel', 'Request $request', ''), ('', 'private', 'init_components', 'Request $request', 'void'), ('', 'private', 'init_payment_transition', 'PaymentType $payment_type', 'void'), ('', 'private', 'get_payment_type', 'string $payment_type_description', 'PaymentType'), ('', 'private', 'get_payment_device', 'Request $request', '')]
    php_code = PHP('./test/test.php')

    assert php_code.get_classes() == php_test_file_classes
    assert php_code.get_properties() == php_test_file_properties
    assert php_code.get_methods() == php_test_file_methods

if __name__ == '__main__':
    _test()