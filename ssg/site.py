import sys
from pathlib import Path


class Site:
    def __init__(self, source, dest, parsers=None):
        self.source = Path(str(source))
        self.dest = Path(str(dest))
        # Available parsers
        self.parsers = parsers or []
        parsers = Site()

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
            # Run the parser
            elif path.is_file():
                self.run_parser(path)

    # Site class load_parser() method
    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser

    # Site class run_parser() method
    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        # Call the parse() method
        if parser is not None:
            parser.parse(path, self.source, self.dest)
        else:
            # Calling error @staticmethod
            # print("Not Implemented")
            self.error("No parser for the {} extension, file skipped!").format(path.suffix)

    # Error reporting @staticmethod
    @staticmethod
    def error(message):
        sys.stderr.write("\x1b[1;31m{}\n").format(message)