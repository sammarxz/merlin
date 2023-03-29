import time
from pathlib import Path

import typer
from rich import print
from rich.console import Console
from rich.progress import track

from merlin.create import Create

app = typer.Typer()
console = Console()


@app.callback()
def callback():
    """
    Merlin Static Site Generator
    """


@app.command()
def generate(project_name: Path):
    """
    Generate project files.

    This command will generate the basic folder structure and default files
    for a new project using the Merlin static site generator.

    Arguments:
    - project_name: Name of the project to be generated.
    """
    try:
        create_instance = Create(project_name)
        project_path = Path(project_name)

        with console.status(f'Creating project {project_name}...'):
            for i, file in enumerate(
                track(
                    create_instance.default_files,
                    description='Creating files...',
                )
            ):
                time.sleep(1)
                safe = project_path.joinpath(file['path'])
                console.log(f'Created file {safe}')

        typer.echo(f'Project {project_path} created successfully')
    except Exception as e:
        print(f'[bold red]{e}![/bold red]')
