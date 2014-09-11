'''
Created on Aug 28, 2014

@author: subhash
'''
import extract_line_feature
class HeadingFinder:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.line_feature = extract_line_feature.LineFeature()
        pass
    
    def getHeadingList(self, line_list):
        
        heading_list = list()
        for index in range(len(line_list)):
            if index >= len(line_list):
                continue
            if index == 0:
                continue
            line = line_list[index]
            prev_line = ""
            if index > 0:
                # get prev line
                prev_line = line_list[index-1]
            next_line = ""
            if index < len(line_list) - 1:
                # get next line
                next_line = line_list[index+1]
                
            # check whether current line is heading or not
            if self.line_feature.is_heading(line, prev_line, next_line):
                heading_list.append(index)
        
        return heading_list