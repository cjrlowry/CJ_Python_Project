#!/usr/bin/env python3
import sys #import system
"""
This function will take a given .txt file and for each line of the .txt file, will calculate the linguistic complexity of each line. This function is intended for use on strings of DNA sequences.

Args:
Filetype '.txt'

Returns:
String of characters for each line of the .txt file as well as the linguistic complexity of the line.

"""

def count_observed_substrings(string, k):
    """
    Count the observed substrings of size k in a given string.

    Args:
    string (str): The input string to count substrings in.
    k (int): The size of the substrings to count.

    Returns:
    int: The number of observed substrings of size k in the input string.
    """
    observed = set() # set to store observed substrings
    for i in range(len(string) - k + 1):
        substring = string[i:i+k] # extract substring of length k
        observed.add(substring) # add substring to set of observed substrings
    observed_result = len(observed) # return number of observed substrings
    return observed_result

def count_possible_substrings(string, k):
    """
    Count the possible substrings of size k in a given string.

    If the length of the string is greater than 4^k,
    return 4^k instead of the total number of possible substrings.

    Args:
    string (str): The input string to count substrings in.
    k (int): The size of the substrings to count.

    Returns:
    int: The number of possible substrings of size k in the input string.
    """
    n = len(string)
    if n > 4**k: #check if the string is larger than 4^k
        possible_result = 4**k #return 4^k
    else:
        possible_result = n - k + 1 # if string is smaller than 4^k, return string size minus k size plus 1 to capture the end character
    return possible_result

#calculate complexity using given functions
def string_complexity(string):
    """
    Calculate the complexity of a given string using the above functions, count_possible_substrings and count_observed_substrings.
    
    Args:
    string (str): The input string to calculate the complexity of.
    
    Returns:
    int: The calculated complexity using a ratio of observed:possible substrings of all sizes.
    """
    possible = 0 # set possible to 0 beforehand
    observed = 0 # set observed to 0 beforehand
    n = len(string) #find the length of the string so we can conduct a for loop for all k

    for k in range(1, n+1): #for loop for all substrings of size k
        possible += count_possible_substrings(string, k) #use possible function
        observed += count_observed_substrings(string, k) #use observed function
        print(possible)
        print(observed)
    complexity = float(observed) / possible
    return complexity

import re #needed for re.match
import os
filename = sys.argv[1] #take system argument as filename

def complexity_cj(filename):
    if os.path.splitext(filename)[1] != '.txt':
        return('Error: Input file must be a .txt file.')
    else:
        with open(filename, 'r') as f: #open the filename argument as a file
            for line in f: #for each line in the file:
                if re.match('^[ACGT]+$', line): #check that this is a DNA string
                    complexity_result = string_complexity(line) #calculate complexity using above function
                    return("Complexity of '" + line.strip() + "': " + str(complexity_result)) #print result and associated string
                else: #if string is not of DNA
                    return("Error: Line '" + line.strip() + "' contains invalid characters. Function is for analysis of DNA only.") #error message
end_result = complexity_cj(filename)
print(end_result)