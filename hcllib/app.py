#!/usr/bin/env python3
import logging

import file.service as fs
import hcl.service as hcl
import terraform.service as tf

import config as cfg


def main():
    """
    Return value

    Run the main logic of the app
    """

    args, config = cfg.setup()
    folder = (args.folder or './modules/aks')
    function = (args.function or 'reference')

    for file in fs.findFiles(folder):
        json = hcl.convertTfFileToJson(file)
        controller(function, json)


def controller(function, json):
    if 'reference' == function:
        variables = tf.getVariableReference(json)
        tf.output(variables)

    elif 'definition' == function:
        variableDefinitions = tf.getVariableDefinition(json)
        tf.output(variableDefinitions)

    elif 'compare' == function:
        variableComparison = tf.compareVariable(json)
        print("Compare", variableComparison, sep='\t')


if __name__ == "__main__":
    # execute only if run as a script
    main()
