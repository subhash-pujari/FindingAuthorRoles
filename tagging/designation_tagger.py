'''
Created on Sep 1, 2014

@author: subhash
'''
import re
class DesignationTagger:
    '''
    classdocs
    '''


    def __init__(self):
        self.filename = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/work_section/work_desig_filt.txt"
        
        self.full_re = "\\s+("
        
        for line in open(self.filename):
            line = line.replace("\n", "")
            line = line.lower()
            self.full_re = self.full_re + line + "|"
        
        self.full_re = self.full_re[:len(self.full_re)-1]
        self.full_re = self.full_re + ")"
        
        
    def design_tagger(self, line):
        
        line = line.lower()
        sub = re.findall(self.full_re, line)
        if len(sub) > 0:
            return sub
        
def main():
    desig_tag = DesignationTagger()
 
    for line in open(desig_tag.filename):
        line = line.replace("\n", "")
        line = line.lower()
        
        print line
        print desig_tag.design_tagger(line)


if __name__ == "__main__":
    main()