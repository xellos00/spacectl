import click
from tabulate import tabulate
from spaceone.core import utils


def print_data(data, output, **kwargs):
    if output == 'quiet':
        _print_quiet(data, **kwargs)
    elif len(data) == 0:
        echo('NO DATA')
    elif output == 'table':
        _print_table(data, **kwargs)
    elif output == 'json':
        _print_json(data, **kwargs)
    elif output == 'yaml':
        _print_yaml(data, **kwargs)


def _print_table(data, **kwargs):
    if 'root_key' in kwargs:
        data = utils.get_dict_value(data, kwargs['root_key'], [])
        del kwargs['root_key']
    headers = kwargs.get('headers', 'keys')
    total_count = kwargs.get('total_count')
    if isinstance(data, dict):
        _print_yaml(data)
    else:
        if len(data) > 0 and not isinstance(data[0], (dict, list, tuple)):
            data = [[v] for v in data]
            click.echo(tabulate(data, tablefmt='presto', headers=['Values']))
        else:
            click.echo(tabulate(data, tablefmt='presto', headers=headers))

        if total_count:
            click.echo()
            click.echo(f' Count: {len(data)} / {int(total_count)}')


def _print_json(data, **kwargs):
    if data == {}:
        click.echo()
    else:
        click.echo(utils.dump_json(data, indent=4))


def _print_yaml(data, **kwargs):
    if data == {}:
        click.echo()
    else:
        click.echo('---')
        click.echo(utils.dump_yaml(data))


def _print_quiet(data, **kwargs):
    results = data["results"]
    for result in results:
        items = list(result.values())
        if len(items) > 1:
            click.echo("Please Selector only one column for quiet output.", err=True)
            exit(1)
        values = list(map(str, items))
        click.echo(" ".join(values), nl=False)
    click.echo()


def echo(message, flag=True, err=False, terminate=False):
    if flag:
        click.echo(message, err=err)
    if terminate:
        exit(1)