import typer
from ssg.site import Site
import ssg.parsers

# Configuration options
def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest,
        # Parser configuration
        # Add available parsers
        "parsers": [ssg.parsers.ResourceParser(),
                    ssg.parsers.MarkdownParser(),
                    ssg.parsers.ReStructuredTextParser()]
    }

    # Build the site
    mysite = Site(**config).build()

# Run typer
typer.run(main)
