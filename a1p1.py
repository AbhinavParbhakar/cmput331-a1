#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023 <<Abhinav Parbhakar>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 1 Student Solution
September 2023
Author: <Abhinav Parbhakar>
"""


import string
from sys import flags


LETTERS = ''.join([u+l for u, l in 
    zip(string.ascii_uppercase, string.ascii_lowercase)])


def get_map(letters=LETTERS):
    """
    Takes in a string containing each letter to map to a number\n
    Returns two dictionaries, one with letter-to-number mapping\n
    The other with number-to-letter mapping\n
    Runs in O(n), n = len(letters)\n
    """
    shift_map = {}
    letter_map = {}

    for i,letter in enumerate(letters):
        shift_map[letter] = i
        letter_map[str(i)] = letter

    return shift_map,letter_map

def encrypt(message: str, key: str):
    """
    Encrypts by using the basis provided in casearCipher.py\n
    Uses the shift number for the key to encrypt by using the shift Dict\n
    Returns the crypted string\n
    """
    global SHIFTDICT,LETTERDICT
    shift_num = SHIFTDICT[key]
    cyphertext = ""
    for i,letter in enumerate(message):
        try:
            letter_key = SHIFTDICT[letter]
            crypt_num = shift_num + letter_key
            if crypt_num >= len(SHIFTDICT):
                crypt_num -= len(SHIFTDICT)
        
            cyphertext += LETTERDICT[str(crypt_num)]
        except:
            cyphertext += letter

    return cyphertext
        


def decrypt(message: str, key: str):
    """
    Inputs a crypted string and returns plain-text\n
    """
    global SHIFTDICT, LETTERDICT
    shift_num = SHIFTDICT[key]
    plaintext = ""
    for i,letter in enumerate(message):
        try:
            letter_key = SHIFTDICT[letter]
            crypt_num = letter_key - shift_num

            if crypt_num < 0:
                crypt_num += len(SHIFTDICT)
            plaintext += LETTERDICT[str(crypt_num)]
        except:
            plaintext += letter

    return plaintext



def test():
    global SHIFTDICT, LETTERDICT 
    SHIFTDICT, LETTERDICT = get_map()
    assert decrypt(encrypt("foo", "g"), "g") == "foo"

if __name__ == "__main__" and not flags.interactive:
    test()