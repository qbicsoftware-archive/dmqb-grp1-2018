import click
import os.path
import sys

class parser():

	@click.command()
	@click.option('--type', nargs=1, help="Type of file",
				  type=click.Choice(["fasta", "fastA", "fastq"]))
	@click.argument('files', nargs=-1, type=click.Path())


	def readFiles(type, files):
		output = None
		types = []
		paths = []

		for filename in files:
			if not os.path.exists(filename):
				print "This file does not exist: %s" % filename
			else:
				paths.append(filename)
				for i in range(len(filename)):			
					if filename[i] == '.':
						types.append(filename[i + 1:])
			output = paths, types
		return click.echo(output)

if __name__ == '__main__':
	parser = parser()
	parser.readFiles()


