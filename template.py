#! /usr/bin/python3 
# 
# Template For Scripts
# 
# 
# Template Version 1.1

import os 
home = os.environ["HOME"]

import argparse


def parse_args ( ):

    # Create Argument Parser
    # TODO Add a fancy description here
    parser = argparse.ArgumentParser(description='') 
    
    # Add Arguments
    # TODO Add arguments
    parser.add_argument('-i', '--input', dest='input', type=str, help='Some input')
    # parser.add_argument('-F', '--force', dest="force", action="store_true", help="Force execution for existing directory (skip mkdir) when setting up new project")
    # parser.add_argument('-d', '--output-directory', dest='output_directory', type=str, default='/media/vinay/Shared Storage/Data/Uncategorized', help='Directory to create new reaper project in')
    # # parser.add_argument('-e', '--extension', type=str, default='mp3', help="Audio extension to use [mp3, wav, ...]")
    # parser.add_argument('-s', '--size', type=str, default='750x480', help="Image size WxH" )
    
    # Parse Args
    args = parser.parse_args()

    return args, parser

def check_args ( args, parser ): 
    
    # TODO Complete
    # Check Condition 
    if not args.input:
        parser.print_help()
        print ( "ERROR: Please provide input" )
        exit()
    else:
        print ( args )

def run ( **kwargs ):
    # TODO What's gonna happen?

    # Finished!
    # TODO Update print statement
    print ("Finished!")
    pass 


if __name__ == "__main__":

    # TODO update this description
    print ( "Running - Fancy Template Script" )

    args, parser = parse_args() 

    check_args ( args, parser )

    kwargs = dict ( args._get_kwargs() )
    run ( **kwargs )
