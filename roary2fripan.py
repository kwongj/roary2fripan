#!/usr/bin/env python
# Script by Jason Kwong
# Script to format Roary output for FriPan

# Usage
from __future__ import print_function
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(
	formatter_class=RawTextHelpFormatter,
	description='Script to format Roary output for FriPan',
	usage='\n  %(prog)s [OPTIONS] <OUTPUT-PREFIX>')
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
strainsFILE = str(args.output) + '.strains'
jsonFILE = str(args.output) + '.json'

import csv
portho = []
desc = []
head = []
temp = []

# Parse CSV
with open(args.input) as csvfile:
	genes = csv.reader(csvfile, delimiter=',', quotechar='"')
	header = next(csvfile)
	for row in genes:
		del row[6:14]
		del row[0:2]
		proteins = row[4:]
		for p in proteins:
			if p:
				p = p.replace("\t",",")			# Fix paralogs separated by tab space
				desc.append([p, str(row[0])])
		print(row)
		row = [x.replace("\t",",") if x != "" else '*' for x in row]
		print(row)
		portho.append(row[1:])

# Fix header
	header = header.replace('"','').strip()
	header = header.split(',')
	del header[6:14]
	del header[0:3]
	header[0] = '# Species'
	header[1] = 'Genes'
	header[2] = 'Alg.-Conn.'
	portho.insert(0,header)

# Setup strains file
	strains = sorted(header[3:])
	b = str(len(str(len(strains))))
	a = "%0" + b + "d"
	strains = [(s + '\t' + str(a % (strains.index(s)+1))) for s in strains]
	strains.insert(0,'ID\tOrder')
	strains = ('\n'.join(map(str, strains)))

# Write proteinortho, descriptions and strains files
with open(porthoFILE, 'wb') as outfile:
	out = csv.writer(outfile, delimiter='\t', lineterminator='\n')
	out.writerows(portho)
print('Writing {} ... '.format(porthoFILE))

desc = sorted(desc)
with open(descFILE, 'wb') as outfile:
	out = csv.writer(outfile, delimiter='\t', lineterminator='\n')
	out.writerows(desc)
print('Writing {} ... '.format(descFILE))

with open(strainsFILE, 'wb') as outfile:
	outfile.write(strains)
print('Writing {} ... '.format(strainsFILE))

print('Done.')
