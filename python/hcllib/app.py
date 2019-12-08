#!/usr/bin/env python3
import logging

from config import setup
from file_service import *
from hcl_helper import *
from tf_service import *


def main():
    """
    Return value

    Run the main logic of the app
    """

    args, config = setup()
    folder = (args.folder or './modules/aks')
    function = (args.function or 'reference')

    for file in findFiles(folder):
        json = convertTfFileToJson(file)
        controller(function, json)


def controller(function, json):
    if 'reference' == function:
        variables = getVariableReference(json)
        output(variables)

    elif 'definition' == function:
        variableDefinitions = getVariableDefinition(json)
        output(variableDefinitions)

    elif 'compare' == function:
        variableComparison = compareVariable(json)
        print("Compare", variableComparison, sep='\t')


if __name__ == "__main__":
    # execute only if run as a script
    main()
