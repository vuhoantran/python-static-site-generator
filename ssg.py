import typer
from ssg.site import Site

# Configuration options
def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest
    }

    # Build the site
    mysite = Site(**config).build()

# Run typer
typer.run(main)
