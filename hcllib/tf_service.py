#!/usr/bin/python3

# install hcltojson from https://github.com/kvz/json2hcl
import os
import logging
import sys
import collections
import re


VARIABLE_SEARCH_PATTERN = "var.*"


def getVariableDefinition(json):
    logging.debug('getVariableDefinition')
    if 'variable' in json.keys():
        logging.debug(json)
        keys = json['variable'].keys()
        return keys


def getVariableReference(json):
    logging.debug('getVariableReference')
    return cleanVariableReference(findVariableReference(json))


def compareVariable(json):
    def compare(x, y): return collections.Counter(x) == collections.Counter(y)
    return compare(getVariableDefinition(json), getVariableReference(json))


def findVariableReference(json):
    logging.debug('findVariableReference')
    variables = []
    keys = json.values()
    for key in keys:
        if type(key) is str:
            if re.match(VARIABLE_SEARCH_PATTERN, key) is not None:
                variables.append(key)
                logging.debug('Found match %s' % key)
        elif type(key) is dict:
            # https://stackoverflow.com/questions/577940/how-can-i-make-this-python-recursive-function-return-a-flat-list
            variables.extend(findVariableReference(key))
    return variables


def removeVar(string):
    logging.debug('removeVar')
    return string.replace('var.', '')


def cleanVariableReference(references):
    logging.debug('cleanVariableReference')
    ref = []
    for reference in list(references):
          #print (reference)
        ref.append(removeVar(reference))
    return ref


def output(array):
    logging.debug('output')
    if array:
        for element in array:
            print(element)
