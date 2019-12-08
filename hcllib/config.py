#!/usr/bin/env python3
from argparse import ArgumentParser
from configparser import SafeConfigParser
from os.path import dirname, join, expanduser
import logging

DEFAULT_LOG_FILE_NAME = 'app.log'
DEFAULT_LOG_LEVEL = logging.WARNING
INSTALL_DIR = dirname(__file__)


def readConfig():
    config = SafeConfigParser()
    config.read([
        join(INSTALL_DIR, 'config.ini')
    ])
    return config


def setup():
    """
    Setup app, returns args and config

    * Load app config from `config.ini`
    * Create command line arguments
    * Configure logging
    """
    config = readConfig()
    args = configureArguments()
    configureLogging(config, args.verbose, args.log)

    debugInput(args)

    return args, config


def configureArguments():
    # Configure arguments for cli

    # TODO: Consider going with [Click](https://github.com/pallets/click)
    ap = ArgumentParser()

    # Add logger option
    ap.add_argument('-v', '--verbose', default=False,
                    action='store_true', help='Increase verbosity')
    ap.add_argument('-l', '--log', default=False,
                    action='store_true', help='Log to file %s' % DEFAULT_LOG_FILE_NAME)
    ap.add_argument('folder', nargs='?')
    ap.add_argument('function', nargs='?')

    return ap.parse_args()


def getLogConfig(config):
    try:
        logLevel = config.get('logger', 'level')
    except:
        logLevel = DEFAULT_LOG_LEVEL

    try:
        logFile = config.get('logger', 'filename')
    except:
        logFile = DEFAULT_LOG_FILE_NAME

    return logLevel, logFile


def configureLogging(config, verbose, file):
        # Config logging using passed args, and config sets default levels

    logLevel, logFile = getLogConfig(config)

    if verbose:
        logLevel = logging.INFO

    if file:
        logging.basicConfig(filename=logFile, level=logging.DEBUG)

    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logLevel
    )


def debugInput(args):
    #logging.info('Number of arguments: %s arguments.' % len(args))
    logging.info('Argument List: %s' % str(args))
