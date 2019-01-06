import click
import json
import csv
import sys


@click.command()
@click.argument('input', type=click.File('rb'))
def cli(input):
    """Dynamodb to CSV

    Convert the aws dynamodb output (Scalar types, JSON) to CSV.

    \b
    Process from stdin:
        dyndb2csv -
    \b
    Process from a file:
        dyndb2csv foo.txt
    """
    data = json.load(input)

    header_keys = get_keys(data['Items'])

    writer = csv.DictWriter(sys.stdout, fieldnames=header_keys)
    writer.writeheader()

    for item in data['Items']:
        i = get_row(item)
        writer.writerow(i)

def get_keys(items):
    head = {}
    for item in items:
        for col in item:
            head[col] = True
    return head.keys()

def get_row(item):
    row = {}
    for col, val in item.items():
        key = list(val.keys())[0]
        if key in ['S','N','BOOL','B']:
            row[col] = val[key]

    return row
