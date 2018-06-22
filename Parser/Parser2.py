from __future__ import print_function

import click


class Config(object):
    # empty constructor
    def __init__(self):
        self.verbose = False


# this is going to create a decorator which passes a config object
# to each of click call backs which is basically decorated by this decorator

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option(
    '--verbose',
    is_falg=True,
    default=False,
    help="Verbose output (print debug statement.")  # in is flag is always false by default
@click.command()
@click.argument(  # input [n] files
    '--files',
    nargs=-1,
    type=click.File('r+')  # r+ means read and write
)
def input_file(files):
    if True:
        return input_file


# Get the filename
@click.argument(
    '--filename',
    tpye=click.Path(exists=True),
    required=True)
def touch(filename):
    click.echo(click.format_filename(filename))


# get the file path
@click.argument(
    '--path',
    nargs=-1,
    type=click.Path()
)
def touch(path):
    for i in file:
        click.echo(touch)


click.help_option()


class parser:
    # empty constructor
    def __init__(self):
        pass

    list = []

    def read_pars(self):
        head = ""
        sequence = ""
        file = open('/Users/najiaahmadi/Desktop/dmqb-grp1-2018/Parser/sequencesMSA.fasta')
        for i in file:
            if i.startswith(">"):
                self.list.append((head, sequence))
                if head != "":
                    head = ""
                    sequence = ""
                head += i[:-2]
            else:
                sequence += i[:-2]

        self.list.append((head, sequence))

        self.list = self.list[1:]

        print(self.list)

        file.close()


if __name__ == "__main__":
    parser = parser()
    parser.read_pars()
