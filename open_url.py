#! /usr/bin/python3 
# 
# Script to open a url in a browser

import os 
home = os.environ["HOME"]

import argparse
from abc import ABC, abstractmethod
import webbrowser

def parse_args ( ):

    # Create Argument Parser
    # TODO Add a fancy description here
    parser = argparse.ArgumentParser(description='A script for automatically opening a new url in the browser') 
    
    # Add Arguments
    parser.add_argument('-i', '--input_url', dest='url', type=str, help='The URL to open')
    parser.add_argument('-b', '--browser', type=str, default='firefox', help="The browser to use [default: firefox]")
    # parser.add_argument('-F', '--force', dest="force", action="store_true", help="Force execution for existing directory (skip mkdir) when setting up new project")
    # parser.add_argument('-d', '--output-directory', dest='output_directory', type=str, default='/media/vinay/Shared Storage/Data/Uncategorized', help='Directory to create new reaper project in')
    # # parser.add_argument('-e', '--extension', type=str, default='mp3', help="Audio extension to use [mp3, wav, ...]")
    # parser.add_argument('-s', '--size', type=str, default='750x480', help="Image size WxH" )
    
    # Parse Args
    args = parser.parse_args()

    return args, parser

def check_args ( args, parser ): 
    
    # Check Condition 
    if not args.url:
        parser.print_help()
        print ( "ERROR: Please provide a url" )
        exit()
    else:
        print ( args )


class Browser ( ABC ):

    @abstractmethod
    def get_key ( self ):
        pass

    @abstractmethod
    def url_is_open ( self, url ):
        pass

    @abstractmethod
    def switch_to_url_tab ( self, url ):
        pass

    def open_url ( self, url ):
        key = self.get_key()
        webbrowser.get ( using=key ).open ( url ) 


class FireFox ( Browser ):

    def get_key ( self ):
        return 'firefox'

    def url_is_open ( self, url ):
        False

    def switch_to_url_tab ( self, url ):
        pass

    
def get_browser ( browser_string ):

    if ( browser_string == "firefox" ):
        return FireFox()
    else:
        print ( "Unknown browser type: [{}]".format ( browser_string ) )
        return None
    

def run ( **kwargs ):
    # Check browser type
    browser = get_browser ( kwargs['browser'] )

    # Check if file is open already in browser
    # TODO
    if browser.url_is_open ( kwargs['url'] ):

        # make that tab active
        pass

    else:
        # If not open: then open that tab
        browser.open_url ( kwargs['url'] )

    # Finished!
    print ("Finished!")
    pass 


if __name__ == "__main__":

    # TODO update this description
    print ( "Running - Open URL Script" )

    args, parser = parse_args() 

    check_args ( args, parser )

    kwargs = dict ( args._get_kwargs() )
    run ( **kwargs )
