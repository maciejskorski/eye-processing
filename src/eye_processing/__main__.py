"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Eye Processing."""


if __name__ == "__main__":
    main(prog_name="eye_processing")  # pragma: no cover
