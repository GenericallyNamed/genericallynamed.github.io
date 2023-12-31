"""Builds HTML files from templates."""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from get_data import get_index
SRC = Path('./src')
TEMPLATES = Path(SRC / 'templates')
BUILD = Path('./build')
print(Path(".").absolute())
print(TEMPLATES)


def render_template(template, output, **kwargs):
    """Renders a template file with the given arguments."""
    env = Environment(loader=FileSystemLoader(TEMPLATES))
    template = env.get_template(str(template.relative_to(TEMPLATES)))
    with open(output, 'w', encoding='utf-8') as f:
        f.write(template.render(**kwargs))

print("Compiling index.html template")

render_template(TEMPLATES / 'index.html', BUILD /
                'index.html', **get_index())
