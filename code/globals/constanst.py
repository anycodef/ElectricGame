# here we save all code for easy manage of result return states
from os import path

EXIT_PROGRAM = 1010110
name_folder_root = "ElectricGame"
path_root_project = path.dirname(__file__).split(name_folder_root)[0] + name_folder_root


description_for_objects = [
    {
        'name': 'Jaula de Faraday',
        'description': 'Es una estructura metálica diseñada para bloquear el campo electromagnético en su interior.',
        'image': {
            'filename': f'{path_root_project}\\src\\liveSavers\\faraday_cage.png',
            'resize_to': (200, 200)
        }
    },
    {
        'name': 'Jaula de Faraday',
        'description': 'Es una estructura metálica diseñada para bloquear el campo electromagnético en su interior.',
        'image': {
            'filename': f'{path_root_project}\\src\\liveSavers\\faraday_cage.png',
            'resize_to': (200, 200)
        }
    }

]
