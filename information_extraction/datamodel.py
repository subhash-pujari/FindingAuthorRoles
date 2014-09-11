'''
Created on Aug 28, 2014

@author: subhash
'''
import heading_finder
from util import resume_util
from util import file_interface
from string_util import StringUtil
from scrap_education import ScrapEducation
from information_extraction.scrap_work import ScrapWork
import random

class Resume:
    
    def __init__(self, filename):
        self.filename = filename
        
        self.heading_finder = heading_finder.HeadingFinder()
        self.resume_util = resume_util.ResumeUtil()
        self.string_util = StringUtil()
        
        self.raw_line_list = self.createLineList(filename)
        self.heading_list = self.createHeadingList()
        self.section_list = self.createSectionList()
        
        
    def getSectionList(self):
        return self.section_list
    
    def createLineList(self, filename):
        line_list = list()
        for line in open(filename):
            line_list.append(line)
        return line_list
    
    def createHeadingList(self):
        heading_list = self.heading_finder.getHeadingList(self.raw_line_list)
        return heading_list
        pass
    
    def createSectionList(self):
        section_list = list()
        
        line_list = self.raw_line_list
        
        # check the index of the lines in the heading list
        for index in self.heading_list:
            
            # get current heading
            heading = line_list[index]
            
            # what is the type of the heading
            type_sec = self.resume_util.findType(heading)
            
            if type_sec == self.resume_util.edu_type or type_sec == self.resume_util.work_type:
                #index of the current heading line in heading list
                current_index = self.heading_list.index(index)
            
                #if the current line is the last heading then there is no heading at the last
                if current_index < len(self.heading_list)-1:
                    next_index = current_index + 1   
                else:
                    next_index = None
                
                # intantiate a section list
                section = Section()
                section.setStart(self.heading_list[current_index])
                if next_index is not None:
                    section.setEnd(self.heading_list[next_index]-1)
                else:
                    section.setEnd(len(self.raw_line_list) - 1)
                    
                section.setType(type_sec)
                section.setHeading(heading)
                
                
                for index in range(section.start, section.end):
                    line = line_list[index]
                    
                    if not self.string_util.is_blank(line):
                        section.line_list.append(Line(line))
                        
                
                section_list.append(section)
                    
        return section_list
                 
class Section:
    def __init__(self):
        self.line_list = list()
        self.start = 0
        self.end = 0
        self.sec_type = None
        self.heading = None
        
    def getLineList(self):
        return self.line_list
    
    def setType(self, sec_type):
        self.sec_type = sec_type
    
    def setStart(self, start):
        self.start = start
    
    def setEnd(self,end):
        self.end = end
        
    def setHeading(self, heading):
        self.heading = heading
        
    def get_section(self):
        str = ""
        for line in self.line_list:
            str = str + line.getLine()
            
        return str
            
class Line:
    def __init__(self, line):
        
        self.line = line
        self.temporal_tags = list()
        self.degree_tags = list()
        self.designation_tags = list()
        self.institution_tags = list()
        
    def getLine(self):    
        return self.line
    
    def getTemporal(self):
        return self.temporal_tags
    
    def getDegree(self):
        return self.degree_tags
    
    def getDesignation(self):
        return self.designation_tags
    
    def getInstitution(self):
        return self.institution_tags


def main():
    path = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/pdfToText2.0/"
    path_output = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/"
    scrap_edu = ScrapEducation()
    scrap_work = ScrapWork()
    fileW_edu = open(path_output + "education_section.txt", "w")
    fileW_work = open(path_output + "work_section.txt", "w")
    file_int = file_interface.FileInterface()
    file_list = file_int.get_file_list(path)
    
    fileW_both_sec = open(path_output + "resume_both_sec.tsv")
    
    count = set()
    count_work = 0
    count_edu = 0
    
    count_both_sec = 0
    file_list = list()
    for line in fileW_both_sec:
        line = line.replace("\n", "")
        file_list.append(line)
    
    print len(file_list)
    
    random_file_list = list()
    while len(random_file_list) < 41:
        index = random.randint(0, len(file_list)-1)
        random_file_list.append(file_list[index])
        
    for index in range(len(random_file_list)):
        
        
        filename = random_file_list[index]
        print filename
        resume = Resume(path + filename)
    
        for section in resume.section_list:
            if section.start < 150 and (section.end - section.start) < 70 and section.sec_type == "work":
                scrap_work.scrap_work(section, filename)
                
            if section.start < 100 and (section.end - section.start) < 50 and section.sec_type == "education":
                scrap_edu.scrap_edu(section, filename)

    


if __name__ == "__main__":
    main()