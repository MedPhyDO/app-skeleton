# -*- coding: utf-8 -*-

"""
Das Hauptmodul 

Startet den Webserver


"""
import sys
import argparse

from app import run

# ----------------------------------------------------------------------------- 
if __name__ == '__main__':
       
    version_info = (0, 1, 0)
    version = '.'.join(str(c) for c in version_info)

    # Initialisieren des parsers und setzen des Hilfetextes
    parser = argparse.ArgumentParser( description='skeleton' )
    
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(version) )
    
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