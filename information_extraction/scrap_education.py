'''
Created on Aug 31, 2014

@author: subhash
'''
from tagging import temporal_tagger
from tagging import degree_tagger
from tagging import designation_tagger
class ScrapEducation:
    
    def __init__(self):
        self.temporal_tag = temporal_tagger.TemporalTagger()
        self.degree_tag = degree_tagger.DegreeTagger()
        self.desig_tag = designation_tagger.DesignationTagger()
        self.path = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/"
        self.edu_file = open(self.path + "edu_section.txt", "w")
        pass
    
    def scrap_edu(self, section, filename):
        
        self.edu_file.write("\n")
        self.edu_file.write(filename + "\n")
        for index in range(len(section.line_list)):
            
            line_obj = section.line_list[index]
            
            line = line_obj.getLine()
            line = line.lower()
            duration = self.temporal_tag.temporal_tagger(line)
            if duration is not None:
                self.edu_file.write(line)
                self.edu_file.write(duration.duration_string() + "\n")
                line_obj.temporal_tags.append(duration)
                
            degree = self.degree_tag.deg_tagger(line)
            if degree is not None:
                line_obj.degree_tags.append(degree[0])
                
            desig = self.desig_tag.design_tagger(line)
            if desig is not None:
                line_obj.desig_tags.append(desig[0])
            
            

            # different cases encoutered
            
            # we have temporal tags but no 
        
        return section
       
       
                
def main():
    
    temp_tag = temporal_tagger.TemporalTagger()
    print temp_tag.temporal_tagger("1998").duration_string()
    
    
if __name__ == "__main__":
    main()