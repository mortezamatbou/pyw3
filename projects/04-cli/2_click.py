import click


@click.command()
@click.argument('name')
@click.option('--age', '-a')
def main(name, age):
    click.echo("{}, {}".format(name, age))


if __name__ == "__main__":
    main()
