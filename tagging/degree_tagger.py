'''
Created on Aug 31, 2014

@author: subhash
'''

import re

class DegreeTagger:
    
    def __init__(self):
        
        
        self.dot_re = ["[a-z]+\.\\s*[a-z]+\.\\s*[a-z]+\.\\s*[a-z]+\.", "[a-z]+\.\\s*[a-z]+\.\\s*[a-z]+\.\\s*[a-z]+", "[a-z]+\.\\s*[a-z]+\.\\s*[a-z]+\.", "[a-z]+\.\\s*[a-z]+\.[a-z]+", "[a-z]+\.\\s*[a-z]+\.", "[a-z]+\.[a-z]+" ]
        
        self.full_re = "("
        for line in open("/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/education_section/education_degree_nodot.tsv"):
            line = line.replace("\n", "")
            self.full_re = self.full_re + line + "|"
        
        self.full_re = self.full_re[:len(self.full_re)-1]
        self.full_re = self.full_re + ")"
        
        self.short_re = "\\s+("
        for line in open("/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/education_section/education_degree_nodot_space.tsv"):
            line = line.replace("\n", "")
            self.short_re = self.short_re + line + "|"
        
        self.short_re = self.short_re[:len(self.short_re)-1]
        self.short_re = self.short_re + ")\\s+"
        
    def deg_tagger(self, line):
        
        line = line.lower()
        
        for re_exp in self.dot_re:
            sub = re.findall(re_exp, line)
            if len(sub) > 0:
                return sub
            
        sub = re.findall(self.full_re, line)    
        if len(sub) > 0:
            return sub
        
        sub = re.findall(self.short_re, line)    
        if len(sub) > 0:
            return sub
        
def main():
    
    deg_tag = DegreeTagger()
    path = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/education_section/"
    #fileW = open(path + "education_degree_nodot.tsv" , "w")
    
    print deg_tag.deg_tagger(" ms ")
    
if __name__ == "__main__":
    main()