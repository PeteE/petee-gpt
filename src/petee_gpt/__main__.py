"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """PeteE GPT."""


if __name__ == "__main__":
    main(prog_name="petee-gpt")  # pragma: no cover
