import typer
from ssg.site import Site
import ssg.parsers

# Configuration options
def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest,
        # Parser configuration
        "parsers": [ssg.parsers.ResourceParser()]
    }

    # Build the site
    mysite = Site(**config).build()

# Run typer
typer.run(main)
