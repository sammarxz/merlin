import os
import shutil

import pytest

from merlin.create import Create


def test_create_should_generate_a_new_merlin_static_site():
    path = 'blog_test'
    template_folder = f'{path}/templates'
    content_folder = f'{path}/content'
    config_file = f'{path}/merlin.yml'

    Create(path)

    assert os.path.exists(path)
    assert os.path.exists(template_folder)
    assert os.path.exists(content_folder)
    assert os.path.isfile(config_file)


def test_create_should_return_file_already_exists():
    path = 'blog_test'

    with pytest.raises(Exception) as excinfo:
        Create(path)

    assert excinfo.value.args[0] == 'Arquivo já existe'
    assert str(excinfo.value) == 'Arquivo já existe'

    shutil.rmtree(path)
