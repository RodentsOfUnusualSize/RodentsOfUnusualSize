#!/usr/bin/python
import sys
import signal
import commands
import socket
import re
import logging as log

log_file = "rous.log"
whitelist = "rous/utils/whitelist.txt"


#
def setup_logger():
    log.basicConfig(filename=log_file,
        format='%(asctime)s %(levelname)s\t%(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        stream=sys.stdout,
        level=log.INFO)
setup_logger()


#
def read_from_whitelist(address):
    try:
        f = open(whitelist, "r")
        lst = [line.split(',') for line in f.readlines()]
        f.close()
        return lst
    except:
        log.error("%s - FAILED to read whitelist",address)


#
def write_to_whitelist(lst, address):
    erase_text_file(whitelist, address)
    try:
        f = open(whitelist, "a")
        if lst:
            for l in lst:
                f.write(l)
                f.write("\n")
        f.close()
    except:
        log.error("%s - FAILED to write to whitelist",address)


#
def erase_text_file(text_file, address):
    try:
        f = open(text_file, 'r+')
        f.truncate()
        f.close()
    except:
        log.error("%s - FAILED to erase text file",address)


#
def handle_crtl_z(address, signal, frame):
    log.info("%s - Crtl Z: Server shutting down",address)
    sys.exit(0)

