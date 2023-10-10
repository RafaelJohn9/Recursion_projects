#!/usr/bin/python3

"""
code is used to find files with some attr that are defined in here as functions
1:  hasEvenByteSize- gives all files that do have even number of bytes
2: hasEveryVowel- gives files that has every vowel in the filename

@Walk:
    this is the main function of this code it contains the main logic of the program
"""

import os

def hasEvenByteSize(fullFilePath):
    """ checks if the files given has even byte size,
    otherwise it returns False"""
    fileSize = os.path.getsize(fullFilePath)
    return fileSize % 2 == 0

def hasEveryVowel(fullFilePath):
    """ checks if the files given has every vowel in it,
    otherwise returns False"""
    name = os.path.basename(fullFilePath).lower()
    return  ('a' in name) and ('e' in name) and ('i' in name) and ('o'in name) and ('u' in name)

def walk(folder, matchedFunc):
    """
    it iteratively searches for the file that returns true for matchedFunc
    and recursively goes into the subdirectories
    """
    # storage of matched files
    matchedFiles = []
    # absolute pathname
    folder = os.path.abspath(folder)

    # iteration in the dir
    for content in os.listdir(folder):
        content = os.path.join(folder, content)
        if os.path.isfile(content):
            if  matchedFunc(content):
                matchedFiles.append(content)
        elif os.path.isdir(content):
            matchedFiles.extend(walk(content, matchedFunc))
    return matchedFiles


if  __name__ == '__main__':
        userinputPath = input('please enter the absolute path of dir to search into: ')
        userinputCmd = input('what would you like to search for:\n\t1.hasEvenByteSize\n\t2.hasEveryVowel\n(enter the number only)\n>>> ')
        cmdDict = {
                '1': hasEvenByteSize,
                '2': hasEveryVowel
                }
        print(walk(userinputPath, cmdDict[userinputCmd]))
