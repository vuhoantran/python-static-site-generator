from pathlib import Path
from typing import List
import shutil
# Markdown and ReStructuredText imports
import sys
from docutils.core import publish_parts
from markdown import markdown
from ssg.content import Content


class Parser():
    extensions: List[str] = []

    # Validate Extensions
    def valid_extension(self, extension):
        return extension in self.extensions

    # Base parse() method
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    # Parser read() method
    def read(self, path):
        with open(str(path), 'r') as file:
            return file.read()

    # Parser write() method
    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)

    # Parser copy() method
    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))


# ResourceParser subclass
class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path, source, dest):
        self.copy(path, source, dest)


# Markdown Parser subclass
class MarkdownParser(Parser):
    extensions = [".md", ".markdown"]

    # Markdown parse() method
    def parse(self, path: Path, source: Path, dest: Path):
        content = Content.load(self.read(path))
        # Converting markdown to html
        html = markdown(content.body)
        self.write(path, dest, html)
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n".format(path.name, content))


# ReStructuredText parser subclass
class ReStructuredTextParser(Parser):
    extensions = [".rst"]

    # ReStructuredText parse() method
    def parse(self, path: Path, source: Path, dest: Path):
        content = Content.load(self.read(path))
        # Converting ReStructuredText to html
        html = publish_parts(content.body, writer_name="html5")
        self.write(path, dest, html["html_body"])
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n".format(path.name, content))
