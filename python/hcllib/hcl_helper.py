#!/usr/bin/python3

import os
import logging
import sys
import subprocess
import json

HCL_TO_JSON = 'hcltojson'
HCL_INSTALL_CMD = './install-hcltojson.sh'


def installHclToJson():
    subprocess.check_output([HCL_INSTALL_CMD])


def hclFileToJson(path):
    logging.debug('Run %s on %s' % (HCL_TO_JSON, path))
    return subprocess.check_output([HCL_TO_JSON, path])


def parseJson(data):
    logging.debug('parseJson %s' % data)
    return json.loads(data)


def convertTfFileToJson(path):
    logging.debug('Read file %s' % path)
    logging.info('Read file %s' % path)
    json_data = hclFileToJson(path)
    return parseJson(json_data)
