'''
Created on Jul 30, 2014

@author: subhash
'''
import re
#from nltk import corpus
from string_util import StringUtil

class ExtractFeature:
    
    def __init__(self):
        #self.stopwords = corpus.stopwords.words('english')
        if "and" in self.stopwords:
            self.stopwords.remove("and")    
        
    def extract_feature_line(self, line):
        pass
    
class LineFeature:
    
    def is_heading(self, line, prev_line, next_line):
        
        
        util = StringUtil()

        if util.is_blank(line):
            return False
        
        is_prev_line_blank = util.is_blank(prev_line)
        is_next_line_blank = util.is_blank(next_line)
        has_stop_words = util.has_stopword(line)
        is_end_with_colon = util.is_end_with_colon(line)
        is_start_with_number = util.is_start_with_number(line)
        has_limited_tokens = util.has_limited_tokens(line, 5)
        has_year = util.has_year(line)
        is_title = util.isTitle(line)
        
        
        #1st - strong case:
        
        # the string is title
        is_title = is_title or is_start_with_number
        one_line_blank = is_prev_line_blank or is_next_line_blank 
        
        if is_title and one_line_blank and not has_stop_words and has_limited_tokens and not has_year:
            return True
        
        return False
        #has_number_in_between = False
         
    def is_line_blank(self, line):
        pass


    
def main():
    pass

if __name__ == "__main__":
    main()