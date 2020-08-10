#!/usr/bin/env python3

import io
import plantuml
import uw.converter
from PIL import Image
from uw.system import get_parameters, get_directory_file_names

def main():
    directory_path, output_path = get_parameters()
    
    if(directory_path and output_path):
        print('Estraggo i file...')
        file_names = get_directory_file_names(directory_path)

        markdown = '@startuml\n'

        for file_name in file_names:
            try:
                plant_uml_converter = uw.converter.PlantUML(file_name)
                markdown += plant_uml_converter.build_entities()
            except (KeyboardInterrupt, SystemExit):
                break
            except Exception as error:
                print(error)

        markdown += '\n@enduml'

        # plant_uml_processor = plantuml.PlantUML(url='http://localhost:8080/plantuml/img/')
        # raw_data = plant_uml_processor.processes( markdown )
        # print(raw_data)

        # stream = io.BytesIO(raw_data)
        file = open('file.txt', 'w')
        print(markdown, file=file)

        # img = Image.open(stream)
        # img.save('foo.png')

        return 0
    else:
        return -1

if __name__ == '__main__':
    main()