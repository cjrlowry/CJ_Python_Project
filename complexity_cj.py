#!/usr/bin/env python3
import sys #import system

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
        possible_result = n - k + 1 # if string is smaller than 4^k, return string size minus k size plus 1
    return possible_result

#calculate complexity using given functions
def complexity(string):
    
    possible = 0 # set possible to 0 beforehand
    observed = 0 # set observed to 0 beforehand
    n = len(string) #find the length of the string so we can conduct a for loop for all k

    for k in range(1, n+1): #for loop for all substrings of size k
        possible += count_possible_substrings(string, k) #use possible function
        observed += count_observed_substrings(string, k) #use observed function

    complexity = observed/possible
    print(complexity)

filename = sys.argv[1]

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        complexity_result = complexity(line)
        print(f"Complexity of '{line}': {complexity_result}")
