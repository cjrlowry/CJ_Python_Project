from complexity_cj import *
"""
This test report will check that the complexity_cj.py script will do the following correctly:
1. Check that the script accurately calculates the complexity of a script with known linguistic complexity.
2. Check that each line in the .txt file contains only ATGC characters for DNA analysis and print an error if not.
3. Check that the input file is a .txt file and print an error if not.
"""



def test_known_string():
    with open('test_input_file.txt', 'w') as f:
        f.write('ATTTGGATT')
    actual_output = complexity_cj('test_input_file.txt')
    #actual_output = string_complexity('ATTTGGATT')
    expected_output = "Complexity of 'ATTTGGATT': 0.875"
    assert actual_output == expected_output

def test_wrong_chars():
    with open('test_input_file.txt', 'w') as f:
        f.write('ATTTGGAT1')
    actual_output = complexity_cj('test_input_file.txt')
    expected_output = "Error: Line 'ATTTGGAT1' contains invalid characters. Function is for analysis of DNA only."
    assert actual_output == expected_output

def test_wrong_filetype():
    with open('test_input_file.tmp', 'w') as f:
        f.write('This is a test file')
    actual_output = complexity_cj('test_input_file.tmp')
    expected_output = 'Error: Input file must be a .txt file.'

import os # remove temporary files
if os.path.exists('test_input_file.tmp'):
    os.remove('test_input_file.tmp') #remove .tmp file
if os.path.exists('test_input_file.txt'):
    os.remove('test_input_file.txt') #remove .txt file