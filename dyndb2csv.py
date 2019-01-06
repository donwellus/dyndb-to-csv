import click
import json


@click.command()
@click.argument('input', type=click.File('rb'))
def cli(input):
    """Dynamodb to CSV

    Convert the aws dynamodb output to CSV.

    \b
    Process from stdin:
        dyndb2csv -
    \b
    Process from a file:
        dyndb2csv foo.txt
    """
    data = json.load(input)
    print(data)