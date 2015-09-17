# roary2fripan
Formats Roary output for viewing in FriPan

## Author
Jason Kwong (@kwongjc)  
GitHub: [kwongj](https://github.com/kwongj)  

## Dependencies
* [Python 2.x](https://www.python.org/downloads/)
* [Roary](https://github.com/sanger-pathogens/Roary)
* [FriPan](http://drpowell.github.io/FriPan/)

## Usage
`$ roary2fripan.py -h`  
```
usage: 
  roary2fripan.py [OPTIONS] <PREFIX>

Script to format Roary output for FriPan

positional arguments:
  PREFIX        Specify output prefix

optional arguments:
  -h, --help    show this help message and exit
  --input FILE  Specify Roary output (default = "gene_presence_absence.csv")
  --version     show program's version number and exit
```

## Basic syntax
Requires output file "gene_presence_absence.csv" from Roary

    $ roary2fripan.py --input gene_presence_absence.csv output

This produces two files:
* output.proteinortho (array of gene presence/absence)
* output.descriptions (annotations for genes)

These two files can be loaded into FriPan for viewing. See links below.

##Bugs
Please submit via the GitHub issues page: [https://github.com/kwongj/roary2fripan/issues](https://github.com/kwongj/roary2fripan/issues)  

##Software Licence
GPLv2: [https://github.com/MDU-PHL/ngmaster/blob/master/LICENSE](https://github.com/MDU-PHL/ngmaster/blob/master/LICENSE)

## Links
* Roary by Andrew Page - [https://github.com/sanger-pathogens/Roary](https://github.com/sanger-pathogens/Roary)
* FriPan by David Powell - [http://drpowell.github.io/FriPan/](http://drpowell.github.io/FriPan/)
