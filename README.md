# splitTextFile

## Introduction

Inspired by the following StackOverflow article.

* Splitting large text file into smaller text files by line numbers using Python
  `https://stackoverflow.com/questions/16289859/splitting-large-text-file-into-smaller-text-files-by-line-numbers-using-python`


## Usage

This Python script was created and tested with version 3.11 on Windows 10 using PowerShell 7 for the command-line. It is intended for splitting up of base64 encoded files. It hasn't been tested on any other, i.e. binary, file formats.

If/when/maybe I have time I will test on other platforms such as Ubuntu.

## Execution

These examples asume the above PowerShell session. Python must obviously be added to the `$env:PATH` variable. There isn't any limitation imposed on this script that would prevent execution in another environment such as Windows Command Prompt (CMD.EXE), Git Bash for Windows or Bash. Note that this script has not been tested on Unix/Linix/POSIX.

### Split a file

Split a base64 text file using the default line count in the output file which will result in output files with a size of 1 MiB each.

`python .\splitFile.py --inFile .\testfile.zip.b64`

### Split a text file and specify the number of lines in each output file.

`python .\splitFile.py --inFile .\testfile.zip.b64 --lines 3`

### Test and verify

I have included a file `testfile.txt` in this repo.

This will split the test file will the default value for number of lines per output file.

`python .\splitFile.py --inFile .\testfile.txt`

The output file is `testfile.txt_13443.txt` as the entire input file is less than 1 MiB in size.

This example will use a more reasonable value for number of lines per output file.

`python .\splitFile.py --inFile .\testfile.txt --lines 3`

The output files are:

* `testfile.txt_03.txt`
* `testfile.txt_06.txt`
* `testfile.txt_09.txt`

## Author

Andrew Nagy

https://www.linkedin.com/in/andrew-e-nagy/
