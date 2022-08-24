# .txt to .xml converter

This small CLA converts files holding information about people in a specific format into a corresponding .xml file.

## Table of contents
1. [Installation](#Installation)
2. [Usage](#Usage)
3. [License](#License)

## Installation

* Requirements: The application is written in Python. Thus Python 3 must be installed to run the programm.
* To install the application, copy the repository to a local drive, using git clone or by downloading an archive.

## Usage
* To start the app, navigate to the root directory and run:
```
python src/main.py 'absolute filepath to input file'
```
If no file is specified as an argument or the path is wrong, the app terminates.
* Input files must be provided in the following format:
```
P|firstname|lastname
T|mobile|telephone
A|street|city|postalnumber
F|name|year
```
P = Person\
T = Phone numbers\
A = Address\
F = Family member\
\
P can be followed by T, A and F\
F can be followed by T and A
* Errors in the fomat let the application terminate by informing the user in which line the (first) error occurred.

## License
The application is licensed under the MIT license. Refer to LICENCE.md for further information.\
\
Copyright 2022 Fabian Fröschl
