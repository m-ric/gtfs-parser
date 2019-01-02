#!/usr/bin/env python3

import csv
import os
import pandas
import sys


# TODO replace dummy log with logging
def log(*args, **kwargs):
	print(*args, **kwargs)


def readCSVColumn(fpath):
	with open(fpath, mode='r') as fp:
		log(f'parsing {fpath}...')
		csv_reader = csv.DictReader(fp)
		nlines = 0

		for row in csv_reader:
			if nlines == 0:
				log(f'Columns:{", ".join(row)}')


def readCSV(fpath):
	with open(fpath, mode='r') as fp:
		log(f'parsing {fpath}...')
		csv_reader = csv.DictReader(fp)
		nlines = 0

		for row in csv_reader:
			if nlines == 0:
				log(f'Columns:{", ".join(row)}')
				nlines += 1

			#log(f'\t{row["name"]})
			nlines +=1

		log(f'{nlines} parsed')


if len(sys.argv) < 2:
	log(f'{sys.argv[0]} <input-dir>')
	sys.exit(1)

inputdir = sys.argv[1]
inputdir = os.path.expanduser(inputdir)

for file_ in os.listdir(inputdir):
	inputfile = os.path.join(inputdir, file_)

	# ignore files not containing the 'route_id' column
	df = pandas.read_csv(inputfile)
	if 'route_id' not in df:
		continue

	log(df)

log("Done")