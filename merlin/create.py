import errno
import os
import shutil

from .config import config_folder, content_folder, template_folder


class Create:
    """
    Class responsible for creating the directory and default file structure
    for a new Merlin project.

    Attributes:
    ----------
    config_path : str
        The path to the 'merlin.yaml' configuration file.
    directories : list
        The list of directory names to be created within the project folder.
    default_files : list
        The list of dictionaries containing information about the default
        files to be created.
        Each dictionary should have the keys 'path' and 'content',
        corresponding to the path to the file and the content of
        the file, respectively.

    Methods:
    --------
    __init__(self, path):
        Initializes the `Create` class with the path to the project to be
        created. Creates the directory structure and default files.

    create_directory_structure(self):
        Creates the directory structure for the project.

    ensure_path_exists(self, path):
        Checks if the specified path exists. If it does not exist,
        creates the directory.

    create_default_files(self):
        Creates the default files for the project.

    safe_path(self, path):
        Returns the absolute path to the specified directory/file,
        avoiding invalid path errors.
    """

    config_path = 'merlin.yaml'
    directories = ['content', 'templates']
    default_files = [
        {'path': 'content/index.md', 'content': content_folder},
        {'path': 'templates/template.j2', 'content': template_folder},
        {'path': 'merlin.yml', 'content': config_folder},
    ]

    def __init__(self, path):
        self.path = path
        self.abspath = os.path.abspath(self.path)

        self.create_directory_structure()
        self.create_default_files()

        return None

    def create_directory_structure(self):
        for path in self.directories:
            safe = self.safe_path(path)
            self.ensure_path_exists(safe)

    def ensure_path_exists(self, path):
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
            pass

    def create_default_files(self):
        for file in self.default_files:
            safe = self.safe_path(file['path'])

            if not os.path.exists(safe):
                shutil.copy2(file['content'], safe)
                # print(f"Criando arquivos {safe}")
            else:
                raise Exception('Arquivo já existe')

    def safe_path(self, path):
        return os.path.join(self.abspath, path)
