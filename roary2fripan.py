#!/usr/bin/env python
# Script by Jason Kwong
# Script to format Roary output for FriPan

# Usage
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(
	formatter_class=RawTextHelpFormatter,
	description='Script to format Roary output for FriPan',
	usage='\n  %(prog)s [OPTIONS] <PREFIX>')
parser.add_argument('output', metavar='PREFIX', help='Specify output prefix')
parser.add_argument('--input', metavar='FILE', default='gene_presence_absence.csv', help='Specify Roary output (default = "gene_presence_absence.csv")')
parser.add_argument('--version', action='version', version=
	'=====================================\n'
	'%(prog)s v0.1\n'
	'Updated 16-Sep-2015 by Jason Kwong\n'
	'Dependencies: Python 2.x\n'
	'=====================================')
args = parser.parse_args()
porthoFILE = str(args.output) + '.proteinortho'
descFILE = str(args.output) + '.descriptions'

import csv
portho = []
desc = []
head = []

# Parse CSV
with open(args.input) as csvfile:
	genes = csv.reader(csvfile, delimiter=',', quotechar='"')
	header = next(csvfile)
	for row in genes:
		del row[6:11]
		del row[0:2]
		proteins = row[4:]
		for p in proteins:
			if p:
				desc.append([p, row[0]])
		row = [x if x != "" else '*' for x in row]
		portho.append(row[1:])

# Fix header
	header = header[:-2]
	header = header.replace('"','').strip()
	header = header.split(',')
	del header[6:11]
	del header[0:3]
	header[0] = '# Species'
	header[1] = 'Genes'
	header[2] = 'Alg.-Conn.'
	portho.insert(0,header)

# Write proteinortho and descriptions files
with open(porthoFILE, 'w') as outfile:
	out = csv.writer(outfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
	out.writerows(portho)
desc = sorted(desc)
with open(descFILE, 'w') as outfile:
	out = csv.writer(outfile, delimiter='\t')
	out.writerows(desc)
