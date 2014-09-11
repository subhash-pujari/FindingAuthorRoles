'''
Created on Aug 31, 2014

@author: subhash
'''
from tagging import temporal_tagger
from tagging import degree_tagger

class ScrapEducation:
    
    def __init__(self):
        self.temporal_tag = temporal_tagger.TemporalTagger()
        self.degree_tag = degree_tagger.DegreeTagger()
        self.path = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/"
        self.edu_file = open(self.path + "edu_section.txt", "w")
        pass
    
    def scrap_edu(self, section, filename):
        
        self.edu_file.write("\n")
        self.edu_file.write(filename + "\n")
        for line in section.line_list:
            
            line = line.getLine()
            line = line.lower()
            duration = self.temporal_tag.temporal_tagger(line)
            
            if duration is not None:
                self.edu_file.write(line)
                self.edu_file.write(duration.duration_string() + "\n")
                print line
                print duration.duration_string()
                if line.find('\xe2'):
                    print list(line)
                
            degree = self.degree_tag.deg_tagger(line)
            if degree is not None:
                print degree[0]
                print line
                
def main():
    
    temp_tag = temporal_tagger.TemporalTagger()
    print temp_tag.temporal_tagger("1998").duration_string()
    
    
if __name__ == "__main__":
    main()