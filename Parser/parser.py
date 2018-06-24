import click
import os.path
import sys

class parser():

	@click.command()
	@click.argument('files', nargs=-1, type=click.Path())	
	#@click.argument('type', nargs=1)
	def readFiles(files):
		output = None
		types = []
		paths = []
		for filename in files:

			if not (os.path.isfile(filename)):
				click.echo("This file does not exist: ")
				click.echo(filename)
				sys.exit(0)
			
			paths.append(filename)
			type = ''
			isFileEnding = False
			for i in filename:
				if isFileEnding:
					type += i				
				if i == '.':
					isFileEnding = True
			types.append(type)
			type = ''
			isFileEnding = False	
			
		output = paths, types
		return click.echo(output)

if __name__ == '__main__':
	parser = parser()
	parser.readFiles()
