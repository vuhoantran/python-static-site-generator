from pathlib import Path
from typing import List
import shutil

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

