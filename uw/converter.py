#!/usr/bin/env python3
import re
from abc import ABC, abstractmethod

_FILE_FORMAT_NOT_SUPPORTED = " format is not supported"

# Exported functions
# UML
class UML_markdown(ABC):
    
    def __init__(self, file_path: str):
        self.__extension = get_extension(file_path)
        
        if(self.__extension == 'php'):
            self._code = PHP(file_path)
        elif(self.__extension == 'vue'):
            self._code = Vue(file_path)
        else:
            raise Exception(self.__extension + _FILE_FORMAT_NOT_SUPPORTED)

        self._markdown = ''

    @abstractmethod
    def build_entities(self):
        pass

    @abstractmethod
    def build_properties(self):
        pass

    @abstractmethod
    def build_methods(self):
        pass

class PlantUML(UML_markdown):

    def build_entities(self) -> str:
        full_class_name = self._code.get_namespace()

        for index, entities in enumerate(self._code.get_entities()):
            class_traits, type, class_name, action, parent = entities
            full_class_name.append( class_name )

            properties = []

            for property in self._code.get_properties():
                property_traits, visibility, property_name = property
                properties.append( property_name )

            methods = []

            for method in self._code.get_methods():
                method_traits, visibility, method_name, parameters, returns = method
                methods.append( method_name + "( " + parameters +  " ): " + returns)

            self._markdown += '\n ' + class_traits + " " + type + " " + '\\'.join(full_class_name) +' { \n ' + '\n'.join(properties) + '\n' + '\n'.join(methods) + ' \n}'
            
            if parent:
                self._markdown += '\n ' + parent + (' <|... ' if action == 'implements' else ' <|--- ') + '\\'.join(full_class_name)

        return self._markdown

    def build_properties(self):
        return self._code.get_properties()

    def build_methods(self):
        return self._code.get_methods()

# Code
class Code(ABC):

    def __init__(self, file_path: str):
        try:    
            self._file_content = open_file(file_path, 'r').read()
        except AttributeError:
            print( open_file(file_path, 'r') )
    
    @abstractmethod
    def split_by_entity(self) -> list:
        pass
    
    @abstractmethod
    def get_namespace(self) -> list:
        pass

    @abstractmethod
    def get_dependencies(self) -> list:
        pass

    @abstractmethod
    def get_entities(self) -> list:
        pass

    @abstractmethod
    def get_properties(self) -> list:
        pass

    @abstractmethod
    def get_methods(self) -> list:
        pass

class PHP(Code):

    __split_by_entities_regex = r'.*class.*|.*interface.*'

    __namespace_regex = r' *namespace +([\\\w]+)'
    __dependencies_regex = r' *use +([\\\w]+)'
    __entities_regex = r' *(\w+)? *(class|interface) +(\w+) *(extends|implements)? *(\w+)?'
    __properties_regex = r'[ \t]+([abstract|static| ]+)? *(protected|public|private)? +\$(?![\w]+\->)(\w+)'
    __methods_regex = r' *([abstract|static| ]+)? *(protected|public|private)? *function +(\w+)\(([\\\w \$]*)\)[: ]*([\\\w]*)'

    def split_by_entity(self) -> list:
        return re.split(self.__split_by_entities_regex, self._file_content)

    def get_namespace(self) -> list:
        return re.findall(self.__namespace_regex, self._file_content)

    def get_dependencies(self) -> list:
        return re.findall(self.__dependencies_regex, self._file_content)

    def get_entities(self) -> list:
        return re.findall(self.__entities_regex, self._file_content)

    def get_properties(self) -> list:
        return re.findall(self.__properties_regex, self._file_content)

    def get_methods(self) -> list:
        return re.findall(self.__methods_regex, self._file_content)

class Vue(Code):

    def split_by_entity(self) -> list:
        pass

    def get_namespace(self) -> list:
        pass

    def get_dependencies(self) -> list:
        pass

    def get_entities(self) -> list:
        return ["test"]

    def get_properties(self) -> list:
        return ["test"]

    def get_methods(self) -> list:
        return ["test"]

# Test functions for module  
def _test():
    _test_PHP_split_data()
    _test_PHP_extract_data()
    _test_UML_markdown_building()

def _test_PHP_split_data():
    test_file_split_number = 3

    php_code = PHP('./test/test.php')

    assert len(php_code.split_by_entity()) == test_file_split_number

def _test_PHP_extract_data():
    test_file_namespace = ['App\\Http\\Controllers']
    test_file_dependencies = ['Illuminate\\Http\\Request', 'Illuminate\\Validation\\Rule', 'App\\Repositories\\Payments\\PayPal\\Response', 'App\\Repositories\\Payments\\RemoteController', 'App\\Repositories\\Payments\\Device', 'App\\Repositories\\Facade\\Invoice', 'App\\Repositories\\Facade\\Offer', 'App\\Events\\OrderCompleted', 'App\\PaymentType', 'App\\PaymentTransition', 'App\\Events\\AddressUpdated']
    test_file_classes = [('abstract', 'class', 'Test', '', ''), ('', 'class', 'PaymentController', 'extends', 'Controller')]
    test_file_properties = [('', 'private', 'order'), ('', 'private', 'remote_controller'), ('', 'private', 'payment_identifier'), ('', 'private', 'order'), ('', 'private', 'remote_controller'), ('', 'private', 'payment_identifier'), ('', 'private', 'payer_identifier'), ('', '', 'registry'), ('', '', 'result'), ('', '', 'state')]
    test_file_methods = [('', 'public', 'create', 'Request $request', ''), ('', 'public', 'return', 'Request $request', ''), ('', 'public', 'execute', 'Request $request', ''), ('', 'public', 'cancel', 'Request $request', ''), ('', 'private', 'init_components', 'Request $request', 'void'), ('', 'private', 'init_payment_transition', 'PaymentType $payment_type', 'void'), ('', 'private', 'get_payment_type', 'string $payment_type_description', 'PaymentType'), ('', 'private', 'get_payment_device', 'Request $request', '')]
    
    code = PHP('./test/test.php')

    assert code.get_namespace() == test_file_namespace
    assert code.get_dependencies() == test_file_dependencies
    assert code.get_entities() == test_file_classes
    assert code.get_properties() == test_file_properties
    assert code.get_methods() == test_file_methods

def _test_UML_markdown_building():
    uml_result = '\nclass Test { \n  \n}\nclass PaymentController { \n  \n}'
    uml_builder = PlantUML('./test/test.php')

    assert uml_builder.build_entities() == uml_result

if __name__ == '__main__':
    from system import open_file, get_extension

    _test()
else:
    from uw.system import open_file, get_extension