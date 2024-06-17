import click


@click.version_option("1.0.0", prog_name="Digging Sync")
@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
@click.option('--age', '-a')
def main(name, age):
    click.echo("{}, {}".format(name, age))


@click.command()
@click.option('--exchange', '-e', default='all', help='list of symbols for exchange or all symbols')
@click.option('--test', '-t', help='Prompt test', prompt="Enter your name")
def pairs(exchange, test):
    click.echo(f"Pairs for {exchange} exchange")
    click.echo(f"Prompt input: {test}")


cli.add_command(main)
cli.add_command(pairs)

if __name__ == "__main__":
    cli()
