'''
Created on Aug 28, 2014

@author: subhash
'''
import re

class ResumeUtil:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.edu = ["education", "degree", "academic", "qualification"]             
        self.work = ["work","appointment", "position", "profession","experience", "job", "employment"]
        self.work_exc = ["workshop", "service", "award", "teaching", "membership", "activities", "societies", "interests", "grant", "network"]
        self.edu_type = "education"
        self.work_type = "work"
        self.other_type = "other"
        
    def findType(self, heading):
        
        heading = heading.lower()
        
        for edu in self.edu:
            sub = re.findall(edu, heading)
            if len(sub) > 0:
                return self.edu_type
            
        work_flag = False
        for work in self.work:
            sub = re.findall(work, heading)
            if len(sub) > 0:
                work_flag = True
                break
            
        if work_flag:
            exclusion_found = False
            for word in self.work_exc:
                if heading.find(word) >= 0:
                    exclusion_found = True
                    break
                    
            if exclusion_found:
                return self.other_type
            else:
                return self.work_type
            
        return self.other_type
    
def main():
    res_util = ResumeUtil()
    print res_util.findType("Education")
    print res_util.findType("professional Experience")
    print res_util.findType("teaching experience")

if __name__ == "__main__":
    main()