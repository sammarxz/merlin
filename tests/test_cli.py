import os
import tempfile
from pathlib import Path

from typer.testing import CliRunner

from merlin.cli import app

runner = CliRunner()


def test_generate():
    with tempfile.TemporaryDirectory() as tmpdir:
        result = runner.invoke(app, ['generate', tmpdir])
        assert result.exit_code == 0

        result_path = Path(tmpdir)

        assert os.path.exists(result_path)

        index_file = result_path.joinpath('content/index.md')
        template_file = result_path.joinpath('templates/template.j2')
        config_file = result_path.joinpath('merlin.yml')

        assert index_file.exists()
        assert template_file.exists()
        assert config_file.exists()
