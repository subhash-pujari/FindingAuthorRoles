'''
Created on Aug 28, 2014

@author: subhash
'''

from util import file_interface
from datamodel import Resume

class FileScrap:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.path = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/pdfToText2.0/"
        file_int = file_interface.FileInterface()
        self.file_list = file_int.get_file_list(self.path)
        self.resume_list = list()
        
    def scrap_file(self):
        for index in range(len(self.file_list)):
            filename = self.file_list[index]
            resume = Resume(self.path + filename)
            self.resume_list.append(resume)
        
    
def main():
    file_scrap = FileScrap()
    file_scrap.scrap_file()
    count_two = 0
    count_one = 0
    count_zero = 0
    path = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/"
    fileW_one = open(path + "resume_one_section.txt", "w")
    fileW_two = open(path + "resume_two_section.txt", "w")
    fileW_zero = open(path + "resume_zero_section.txt", "w")
    fileW_start_work = open(path + "resume_work_start.txt", "w")
    fileW_start_edu = open(path + "resume_edu_start.txt", "w")
    fileW_length_edu = open(path + "resume_edu_length.txt", "w")
    fileW_length_work = open(path + "resume_work_length.txt", "w")
    
    start_work = dict()
    start_edu = dict()
    length_edu = dict()
    length_work = dict()
    
    
    for resume in file_scrap.resume_list:
        
        if len(resume.section_list) > 1:
            count_two = count_two + 1
            #fileW_two.write(resume.filename + "\n")
            for section in resume.section_list:
                fileW_two.write(section.heading+ "\t" + section.sec_type + "\n")
                
        elif len(resume.section_list) == 1:
            count_one = count_one + 1
            fileW_one.write(resume.filename + "\n")
            
        else:
            count_zero = count_zero + 1
            fileW_zero.write(resume.filename + "\n")
            
        if section.sec_type == "work":
            #fileW_start_work.write(str(resume.filename) + "\n")
            #fileW_start_work.write(str(section.start) + "\n")
            
            if section.start not in start_work:
                start_work[section.start] = 0
            start_work[section.start] = start_work[section.start] + 1
            #fileW_length_work.write(str(resume.filename) + "\n")
            #fileW_length_work.write(str(section.end - section.start) + "\n")
            
            if (section.start - section.end) not in length_work:
                length_work[(section.start - section.end)] = 0
            length_work[(section.start - section.end)] = length_work[(section.start - section.end)] + 1
            
        
        elif section.sec_type == "education":
            #fileW_start_edu.write(str(resume.filename) + "\n")
            #fileW_start_edu.write(str(section.start) + "\n")
            if section.start not in start_edu:
                start_edu[section.start] = 0
            start_edu[section.start] = start_edu[section.start] + 1
            
            
            #fileW_length_edu.write(str(resume.filename) + "\n")
            #fileW_length_edu.write(str(section.end - section.start) + "\n")
            if (section.start - section.end) not in length_edu:
                length_edu[(section.start - section.end)] = 0
            length_edu[(section.start - section.end)] = length_edu[(section.start - section.end)] + 1
            
            print "section_start>>" + str(section.start)
            print "section_end_start>>" + str(section.end - section.start)
            if section.start < 100 and (section.end - section.start) < 70:
                section.print_section()
                pass
    '''
    for start in start_edu:
        fileW_start_edu.write(str(start) + "\t" + str(start_edu[start])+"\n")
    
    for start in start_work:
        fileW_start_work.write(str(start) + "\t" + str(start_work[start])+"\n")
            
    for start in length_edu:
        fileW_length_edu.write(str(start) + "\t" + str(length_edu[start])+"\n")
    
    for start in length_work:
        fileW_length_work.write(str(start) + "\t" + str(length_work[start])+"\n")
    '''
    
if __name__ == "__main__":
    main()
        