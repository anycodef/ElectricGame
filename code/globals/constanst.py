# here we save all code for easy manage of result return states
from os import path
from os.path import join

EXIT_PROGRAM = 1010110
BACK_CODE = 2212122
name_folder_root = "ElectricGame"
path_root_project = path.dirname(__file__).split(name_folder_root)[0] + name_folder_root


description_for_objects = [
    {
        'name': 'Jaula de Faraday',
        'description': 'Es una estructura metálica diseñada para bloquear el campo electromagnético en su interiorelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interio.',
        'image': {
            'filename': join(path_root_project, 'src', 'rules', 'gift.png')
        }
    },
    {
        'name': 'Jaula de Faraday',
        'description': 'Es una estructura metálica electromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interio Ldiseñada para bloquear el campo electromagnético en su interior.',
        'image': {
            'filename': join(path_root_project, 'src', 'rules', 'course.png')
        }
    },
    {
        'name': 'Jaula de Faraday',
        'description': 'Es una estructura metálica diseñada para bloquear el campo electromagnético en su interiorelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interioelectromagnético en su interio.',
        'image': {
            'filename': join(path_root_project, 'src', 'rules', 'character.png')
        }
    },
    {
        'name': 'Jaula de Faraday',
        'description': ' interioelectromagnético en su interio.',
        'image': {
            'filename': join(path_root_project, 'src', 'rules', 'battery.png')
        }
    }
]
