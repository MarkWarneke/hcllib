#!/usr/bin/python3

import os
import logging
import sys
import json


# Search criteria for finding Terraform files
FILE_ENDSWITH_FILTER = '.tf'


def exist(path):
    logging.debug('exist')
    return os.path.isdir(path) or os.path.isfile(path)


def findFiles(path):
    """"
    Searches given `path` for matching files

    - If location does not exist return error
    - Single File will be returned
    - Search dir for matching files `FILE_ENDSWITH_FILTER` e.g. `.tf`
    """
    logging.debug('findFiles')
    results = []

    if not exist(path):
      logging.error('Path %s not found' % path)
      sys.exit('Path %s not found' % path)

    # Singe file
    if os.path.isfile(path):
        logging.debug('Singe file found %s' % path)
        results.append(path)
        return results

    # Search directory search for files
    for root, dirs, files in os.walk(path):
        logging.debug(files)
        for file in files:
            logging.debug(file)
            if file.endswith(FILE_ENDSWITH_FILTER):
                logging.info(file)
                results.append(os.path.join(root, file))

    return results
