import os

DEFAULT_PATH = 'defaults'

cwd = os.path.dirname(os.path.abspath(__file__))

content_folder = f'{cwd}/{DEFAULT_PATH}/index.md'
template_folder = f'{cwd}/{DEFAULT_PATH}/template.j2'
config_folder = f'{cwd}/{DEFAULT_PATH}/merlin.yml'
