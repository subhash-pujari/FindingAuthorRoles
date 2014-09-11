import re
from nltk import corpus
'''
Created on Jul 24, 2014

@author: subhash
'''

class StringUtil:
    
    def __init__(self):
        self.stopwords = corpus.stopwords.words('english')
        if "and" in self.stopwords:
            self.stopwords.remove("and")
    
    def has_year(self, line):
        search = re.findall(r'\d{4}', line)
        if len(search) > 0:
            return True
        return False
    
    def isTitle(self, line):
        
        line = line.replace(" ", "")
        
        sub = re.findall(r'^[A-Z]', line)
        if len(sub) > 0:
            return True
        return False
    
    def has_stopword(self,line):
        word_list = line.split(' ')
        filtered_words = [w for w in word_list if w in self.stopwords]
        if len(filtered_words) > 0:
            return True
        return False
    
    def is_blank(self,line):
        sub = re.findall('[0-9a-zA-Z]', line)
        if(len(sub) > 0):
            return False
        return True
        
    def is_start_with_number(self, line):
            
        s  =  re.findall(r'^([0-9]{1}\.)', line)
        if len(s) > 0:
            return True
        return False
    
    def is_end_with_colon(self,line):
        s  =  re.findall(r':$', line)
        if len(s) > 0:
            return True
        return False
    
    def has_limited_tokens(self, line, n):
        line = line.strip()
        tokens = line.split(' ')
        if len(tokens) > n:
            return False
        return True
    
def test_feature_extractor():
    

    str_util = StringUtil()
    
    
    # test blank line
    line = "\n \t"
    print "is blank>>" + line
    print str_util.is_blank(line)
    
    # test has stopwords
    line = "he is going"
    print "has stopwords>>" + line
    print str_util.has_stopword(line)
    
    # test is end with colon
    
    line = "1. Education:"
    print "end with colon>>" + line
    print str_util.is_end_with_colon(line)
    
    
    # test is start with number
    line = "2. Professional Experience"
    print "start with number>>" + line
    print str_util.is_start_with_number(line)
    
    # limited tokens
    line = "Education in this world"
    print "limited tokens>>" + line
    print str_util.has_limited_tokens(line, 4)
    
    # has year in the string
    line = "masters in 1994 .,"
    print "has year>>" + line
    print str_util.has_year(line)
    
    # is title 
    line = "  Education Title"
    print "is title >>" + line
    print str_util.isTitle(line)
    
    
def main():
    test_feature_extractor()
    
    pass
    
if __name__ == "__main__":
    main()