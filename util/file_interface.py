'''
Created on Jul 22, 2014

@author: subhash
'''
from os import path
from os import listdir
from os.path import isfile, join


class FileInterface(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.path = ""
        
    def get_file_list(self, directory):
        
        if not path.exists(directory):
            return None
            print "the directory doesn't exist"
        
        filename_list = [ f for f in listdir(directory) if isfile(join(directory,f)) ]
        return filename_list