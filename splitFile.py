'''
Inspired by code and comments in the following StackOverflow article:

Splitting large text file into smaller text files by line numbers using Python
https://stackoverflow.com/questions/16289859/splitting-large-text-file-into-smaller-text-files-by-line-numbers-using-python
'''

import argparse
import base64
import os
from pathlib import Path
import math


# https://docs.python.org/3.7/library/argparse.html
parser = argparse.ArgumentParser( description='Encode input file to base64 or decode base64 file to outputfile. Based on https://stackoverflow.com/questions/11511705/base64-encode-a-zip-file-in-python.')
parser.add_argument('--inFile',   type=argparse.FileType('rb'),                  nargs='+', help='Name of input file.' )
parser.add_argument('--lines',    type=int,                      default=13443,  nargs='?', help='The number of lines per output file. Default is (1024*1024) / 78 = 13443 which will split a base64 file into files of 1 MiB in size.' )

args = parser.parse_args()
inputFile           = args.inFile
outputFileLineCount = args.lines

if inputFile is None:
    print( "ERROR: no input file namespecified. Exiting script '" + os.path.basename(__file__) + "'." )
    # https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used
    raise SystemExit

#print( "" )
#print( f"inputFile          = {inputFile},         type = {type(inputFile)}" )
#print( f"inputFile[0]       = {inputFile[0]},      type = {type(inputFile[0])}" )
#print( f"inputFile[0].name  = {inputFile[0].name}, type = {type(inputFile[0].name)}" )

# https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
inputFileOsPath = Path( inputFile[0].name )

#print( f"inputFileOsPath    = {inputFileOsPath},         type = {type(inputFileOsPath)}" )

if inputFileOsPath.is_file():
    # file exists
    print( f"Found input file {inputFileOsPath}." )
else:
    print( f"ERROR: Not found input file {inputFileOsPath[0].name}. Exiting script '" + os.path.basename(__file__) + "'."  )
    raise SystemExit

inputFileSizeBytes = os.path.getsize( inputFileOsPath )
#print( f"inputFileSizeBytes = {inputFileSizeBytes}" )

# https://stackoverflow.com/a/1019572
with open( inputFileOsPath , "rb" ) as f:
    num_lines = sum(1 for _ in f)
#print( f"num_lines = {num_lines}" )

outputFileCount =  math.ceil(num_lines / outputFileLineCount)  
#print( f"outputFileCount = {outputFileCount}" )

outputFileCountFieldWidth = len( str( num_lines ) ) + 1
#print( f"outputFileCountFieldWidth = {outputFileCountFieldWidth}" )

# https://stackoverflow.com/a/16290885
lines_per_file = outputFileLineCount
smallfile = None
with open( inputFileOsPath ) as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
#            small_filename = ( str(inputFileOsPath)  + '_{}.txt' ).format(lineno + lines_per_file)
            outputFileNumberFormatted = str( lineno + lines_per_file ).zfill(outputFileCountFieldWidth)
            print( f" outputFileNumberFormatted = {outputFileNumberFormatted}" )
            small_filename = ( str(inputFileOsPath)  + '_{}.txt' ).format(outputFileNumberFormatted)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()