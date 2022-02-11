import re

import yaml
from yaml import load, FullLoader
from collections.abc import Mapping

# Content class
class Content(Mapping):
    # r for raw string
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    # Load class method
    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    # Content constructor
    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    # Body property
    @property
    def body(self):
        return self.data["content"]

    # Type property
    @property
    def type(self):
        return self.data["type"] if "type" in self.data else None

    # Type setter
    @type.setter
    def type(self, type):
        self.data["type"] = type

    # Custom getitem method
    def __getitem__(self, key):
        return self.data[key]

    # Custom iterator method
    def __iter__(self):
        iter(self.data)

    # Custom length method
    def __len__(self):
        return len(self.data)

    # Content representation
    def __repr__(self):
        data = {}
        # Removing content from the representation
        for key, value in self.data.items():
            if key != "content":
                data[key] = value
        return str(data)


