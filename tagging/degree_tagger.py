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
        
        
    def deg_tagger(self, line):
        
        line = line.lower()
        
        for re_exp in self.dot_re:
            sub = re.findall(re_exp, line)
            if len(sub) > 0:
                return sub
            
        sub = re.findall(self.full_re, line)    
        
        if len(sub) > 0:
            return sub
        
def main():
    
    deg_tag = DegreeTagger()
    path = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/education_section/"
    #fileW = open(path + "education_degree_nodot.tsv" , "w")
    
    for line in open(path + "education_degree_list.txt"):
        line = line.lower()
        line = line.replace("\n", "")
        deg_tag_list = deg_tag.deg_tagger(line)
        
        if deg_tag_list is not None:
            print deg_tag_list
        #else:
        #    fileW.write(line + "\n")
    
if __name__ == "__main__":
    main()