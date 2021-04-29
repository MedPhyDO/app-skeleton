# -*- coding: utf-8 -*-

"""
Das Hauptmodul 

Startet den Webserver


"""
import sys
import argparse

from version import __version__
from app import run

# ----------------------------------------------------------------------------- 
if __name__ == '__main__':

    # Initialisieren des parsers und setzen des Hilfetextes
    parser = argparse.ArgumentParser( description='skeleton' )
    
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__) )
    
    parser.add_argument( "-w", "--webserver",
        action="store_true",
        default=False,
        help="Startet den Webserver",
    )
        
    # ohne Angaben immer webserver
    args = None
    if len( sys.argv ) == 1:
        args = ["--webserver"]

    # Parse commandline arguments
    # unterbindet exit bei help und version
    try:
        args = parser.parse_args( args )
    except SystemExit:
        args=None
        
    if args:
        if args.webserver:
            run()
