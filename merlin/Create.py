import errno
import os
import shutil

from .config import config as cfg
from .config import content, cwd, template


class Create:
    config_path = 'merlin.yaml'
    directories = ['content', 'templates']
    default_files = [
        {'path': 'content/index.md', 'content': '%s/%s' % (cwd, content)},
        {
            'path': 'templates/template.j2',
            'content': '%s/%s' % (cwd, template),
        },
        {'path': 'merlin.yml', 'content': '%s/%s' % (cwd, cfg)},
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
