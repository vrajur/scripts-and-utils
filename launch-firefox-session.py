#! /usr/bin/python3 
# 
# Firefox session launch
# Opens a list of urls
# 
# Template Version 1.1

import os 
home = os.environ["HOME"]

import argparse
import subprocess



def parse_args ( ):

    # Create Argument Parser
    # TODO Add a fancy description here
    parser = argparse.ArgumentParser(description='') 
    
    # Add Arguments
    # TODO Add arguments
    default_path = "/home/vinay/my-firefox-sessions/blog.txt"
    parser.add_argument('-i', '--input', dest='input_tabs_file', type=str, default=default_path, help='File path to file with session tabs')
    # parser.add_argument('-l', '--launch', dest="launch", action="store_true", help="Launch tabs in firefox")
    parser.add_argument('-e', '--edit', dest="edit", action="store_true", help="Edit tabs file")

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
    if not args.input_tabs_file:
        parser.print_help()
        print ( "ERROR: Please provide input tabs file" )
        exit()
    else:
        print ( args )

def edit_tabs_file( input_tabs_file ):

    cmd = f"code {input_tabs_file}"
    ret = subprocess.Popen ( cmd.split(' ') )

def parse_urls ( input_tabs_file ):

    with open(input_tabs_file, 'r') as f:

        windows = []

        window_urls = []
        for line in f.readlines():
            line = line.strip()
            if not line:
                windows.append(window_urls)
                window_urls = []
            else:
                window_urls.append(line)

        windows.append(window_urls)

    return windows

def launch_tabs ( windows ):

    for window in windows:
        # cmd = "firefox -new-tab -url https://www.evernote.com/Home.action -new-tab -url http://www.gmail.com"
        cmd = "firefox "
        cmd += " -new-tab -url ".join(window)
        print (cmd)
        ret = subprocess.Popen ( cmd.split(' ') )
    

        

def run ( **kwargs ):
    # TODO What's gonna happen?
    print(kwargs['input_tabs_file'])

    if kwargs['edit']:
        edit_tabs_file(kwargs['input_tabs_file'])
    else:
        windows = parse_urls(kwargs['input_tabs_file'])
        launch_tabs ( windows )

    # Finished!
    # TODO Update print statement
    print ("Finished!")
    pass 


if __name__ == "__main__":

    # TODO update this description
    print ( "Running - Firefox tab session launcher" )

    args, parser = parse_args() 

    check_args ( args, parser )

    kwargs = dict ( args._get_kwargs() )
    run ( **kwargs )
