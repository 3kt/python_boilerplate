import logging

import click

from utils import Logger

log = Logger()


@click.command()
@click.option("--debug", is_flag=True)
def main(debug):

    log.setLevel(logging.DEBUG if debug else logging.INFO)
    log.info("Started application")


if __name__ == "__main__":
    main()
