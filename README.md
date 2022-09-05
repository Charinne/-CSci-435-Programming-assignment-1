# -CSci-435-Programming-assignment-1
A script that highlights leaf nodes from dumped xml from a png


to run this code you must have Pillow and beautiful soup 4 libraries installed for python. Have a directory with pngs and their dumped xml like the one given with the project description.

You can instal both libraries with the following commands:

pip install beautifulsoup4

pip install Pillow==5.3.0

after downloading the script and libraries, run the code with:

python3 xml.py <path to file with xml and pngs>

example:

python3 xml.py /Users/exampleuser/Desktop/Programming-Assignment-Data
  
  
  
DESCRIPTION:

This code works by using bs4's findall command for 'node', which returns a list of tags which are each node in the xml hierarchy. The nodes tag includes all child nodes, so nodes with no children are leafs. the leafs are located by searching through the list of tags of entries with one occurance of 'node' and 'bounds.'the bounds of these leaf nodes are handed to Pillows Image and ImageDraw objects as bounds for yellow rectangles over the png. the annotated images are then saved using the convention <xml-file-name>.highlighted.png.
  
