# here we save all code for easy manage of result return states
from os import path

code_return = {
    'exitProgram': 1,
    'executeState': 2
}

name_folder_root = "ElectricGame"
path_root_project = path.dirname(__file__).split(name_folder_root)[0] + name_folder_root

