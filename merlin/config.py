import os

DEFAULT_PATH = 'defaults'

cwd = os.path.dirname(os.path.abspath(__file__))
content = f'{DEFAULT_PATH}/index.md'
template = f'{DEFAULT_PATH}/template.j2'
config = f'{DEFAULT_PATH}/merlin.yml'
