'''
Created on Aug 31, 2014

@author: subhash
'''
from tagging import temporal_tagger, designation_tagger
from tagging import degree_tagger

class ScrapWork:
    
    def __init__(self):
        self.temporal_tag = temporal_tagger.TemporalTagger()
        self.desig_tag = designation_tagger.DesignationTagger()
        self.path = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/"
        self.work_file = open(self.path + "work_section.txt", "w")
        pass
    
    def scrap_work(self, section, filename):
        
        self.work_file.write("\n")
        self.work_file.write(filename + "\n")
        for line in section.line_list:
            
            line = line.getLine()
            line = line.lower()
            duration = self.temporal_tag.temporal_tagger(line)
            
            if duration is not None:
                #self.work_file.write(line)
                #self.work_file.write(duration.duration_string() + "\n")
                print duration.duration_string()
                print line
                
            desig = self.desig_tag.design_tagger(line)
            if desig is not None:
                print desig
                print line
                
def main():
    pass
    
    
if __name__ == "__main__":
    main()