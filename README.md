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

    $ roary2fripan.py --input gene_presence_absence.csv <prefix>

This produces three files:
* \<prefix\>.proteinortho (array of gene presence/absence)
* \<prefix\>.descriptions (annotations for genes)
* \<prefix\>.strains (list of strains - can be re-ordered and categories added for displaying in FriPan)

These three files can be loaded into FriPan for viewing. See links below.

##Bugs
Please submit via the GitHub issues page: [https://github.com/kwongj/roary2fripan/issues](https://github.com/kwongj/roary2fripan/issues)  

##Software Licence
GPLv2: [https://github.com/kwongj/roary2fripan/blob/master/LICENSE](https://github.com/kwongj/roary2fripan/blob/master/LICENSE)

## Links
* Roary by Andrew Page - [https://github.com/sanger-pathogens/Roary](https://github.com/sanger-pathogens/Roary)
* FriPan by David Powell - [http://drpowell.github.io/FriPan/](http://drpowell.github.io/FriPan/)
