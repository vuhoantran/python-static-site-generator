from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self.source = Path(str(source))
        self.dest = Path(str(dest))

    def create_dir(self, path):
        # Find root directory
        directory = self.dest / path.relative_to(self.source)

        # Make a directory
        directory.mkdir(parents=True, exist_ok=True)

    # Make the destination directory
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)

        # Recreate all paths
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
