import os
import tempfile

import pytest

from merlin.create import Create


def test_create_should_generate_a_new_merlin_static_site():
    with tempfile.TemporaryDirectory() as tmpdir:
        create_instance = Create(tmpdir)

        for path in create_instance.directories:
            assert os.path.exists(os.path.join(tmpdir, path))

        for file in create_instance.default_files:
            assert os.path.exists(os.path.join(tmpdir, file['path']))


def test_create_should_raise_exception_when_file_already_exists():
    with tempfile.TemporaryDirectory() as tmpdir:
        Create(tmpdir)
        with pytest.raises(Exception) as excinfo:
            Create(tmpdir)

    assert excinfo.value.args[0] == 'File already exists'
    assert str(excinfo.value) == 'File already exists'
