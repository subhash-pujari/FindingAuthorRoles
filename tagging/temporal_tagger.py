# -*- coding: utf-8 -*-

import duration_extraction
import re

class TemporalTagger:
    
    def __init__(self):
        '''
         This class tag the temporal data in the line.
        '''
        # format for months
        self.months = '(january|february|march|april|may|june|august|september|october|november|december|jan|feb|mar|apr|may|june|jun|july|jul|aug|sept|sep|oct|nov|dec)'
        self.month_num = "[0-9]{1,2}"
        self.year_full = "[0-9]{4}"
        self.year_half = "[0-9]{2}"
        
        self.parenthesis_begin = "("
        self.parenthesis_end = ")"
        
        # year month delimiter
        self.year_month_sep = {'forward_slash':'/', 'dot':'\.', 'space':" "}
        # character 
        self.duration_sep = {'hyphen':'-', 'hyphen_non_ascii':'\xe2\x80\x93', 'curly_hyphen':'~','to':' to ' , 'space': ' '}

        #space
        self.space_limitless = "\\s{0,5}"
        
        self.is_month_year = [True, False]
        
        pass
    
    def get_month_year_num(self, sep, is_month_year, is_year_4):   
        '''
            It returns the month year in to format based on parameters passed to the function in which case month is a number.
            
            parameters:
            sep: separator which separates month and year string like '.', ' ', '/'
            is_month_year: whether month year or year month format for the strings with the separator as sep
            is_year_4: whether the year string is of length 2 like 98, 99 or 4 digit like 1994, 1999.
        '''
        
        if is_month_year:
            if is_year_4:
                month_year = self.month_num + sep + self.year_full
            else:
                month_year = self.month_num + sep + self.year_half
        else: 
            if is_year_4:
                month_year = self.year_full + sep + self.month_num
            else:
                month_year = self.year_half + sep + self.month_num
        return month_year
    
    
    
    def get_month_year_str(self, sep, is_month_year, is_year_4):
        
        '''
            It returns the month year in to format based on parameters passed to the function in which case month is a string.
            
            parameters:
            sep: separator which separates month and year string like '.', ' ', '/'
            is_month_year: whether month year or year month format for the strings with the separator as sep
            is_year_4: whether the year string is of length 2 like 98, 99 or 4 digit like 1994, 1999.
        '''
        
        if is_month_year:
            if is_year_4:
                month_year = self.months + sep + self.space_limitless + self.year_full
            else:
                month_year = self.months + sep + self.space_limitless + self.year_half
        else: 
            if is_year_4:
                month_year = self.year_full + sep + self.space_limitless + self.months
            else:
                month_year = self.year_half +  sep + self.space_limitless + self.months
                
        return month_year
        
    
    def get_full_re_exp(self, dur_sep, month_year_sep, is_month_year, is_year_4, is_month_num):
        '''
            returns the full duration regular expression string.
            
            dur_sep - separator between the duration 
            month_year_seperator - separator between month and year string
            is_month_year - is the string representing month, year is in format month year or year month
            is_year_4 - is year of length 2 or 4
            is_month_num - whether the month is a number or a string
        '''
        
        if is_month_num:
            month_year = self.get_month_year_num(month_year_sep, is_month_year, is_year_4)
            full_re_exp = month_year + self.space_limitless + dur_sep + self.space_limitless + month_year
        else:
            month_year = self.get_month_year_str(month_year_sep, is_month_year, is_year_4)
            full_re_exp = month_year + self.space_limitless + dur_sep + self.space_limitless + month_year
        
        full_re_exp = self.parenthesis_begin + full_re_exp + self.parenthesis_end
        return full_re_exp
    
    def get_half_re_exp(self, dur_sep, month_year_sep, is_month_year, is_year_4, is_month_num):
        
        '''
            returns the full duration regular expression string.
            
            dur_sep - separator between the duration 
            month_year_seperator - separator between month and year string
            is_month_year - is the string representing month, year is in format month year or year month
            is_year_4 - is year of length 2 or 4
            is_month_num - whether the month is a number or a string
        '''
        
        if is_month_num:
            month_year = self.get_month_year_num(month_year_sep, is_month_year, is_year_4)
            half_re_exp = month_year + self.space_limitless + dur_sep 
        else:
            month_year = self.get_month_year_str(month_year_sep, is_month_year, is_year_4)
            half_re_exp = month_year + self.space_limitless + dur_sep
            half_re_exp = self.parenthesis_begin + half_re_exp + self.parenthesis_end
        return half_re_exp
    
    # temporal tag full
    def temporal_tag_full(self, line):
        
        '''
            This is temporal full length string.
        '''
        for str_type in ['full', 'year_duration' , 'half', 'year']:
            for dur_sep in self.duration_sep:
                dur_sep = self.duration_sep[dur_sep]
                for month_year_sep in self.year_month_sep:
                    month_year_sep = self.year_month_sep[month_year_sep]
                    for is_month_year in {True, False}:
                        for is_year_4 in {True, False}:
                            for is_month_num in {True, False}:
                                                                
                                if str_type is 'full':
                                    re_exp = self.get_full_re_exp(dur_sep, month_year_sep, is_month_year, is_year_4, is_month_num)
                                elif str_type is 'half':
                                    re_exp = self.get_half_re_exp(dur_sep, month_year_sep, is_month_year, is_year_4, is_month_num)
                                elif str_type is 'year':
                                    re_exp = '[0-9]{4}'
                                elif str_type is 'year_duration':
                                    re_exp = '[0-9]{4}'+ self.space_limitless + dur_sep + self.space_limitless + '[0-9]{4}'
                                
                                sub = re.findall(re_exp, line)
                                if len(sub) > 0:
                                    temporal_tags = duration_extraction.TemporalTags(sub, str_type, dur_sep, month_year_sep, is_month_year, is_year_4, is_month_num)
                                    return duration_extraction.DurationExtraction().duration_extraction(temporal_tags)
        
    def replace_multiple_character(self, source, target, line ):
        line = re.sub(source, target, line)
        return line
    
    
    def temporal_tagger(self, line):
        '''
            The main function to check different kind of temporal tags within the text that we are analysing.
        '''
        
        line = self.replace_multiple_character('\s+', ' ', line)
        if self.temporal_tag_full(line) is not None:
            #print line
            return self.temporal_tag_full(line)
            
        
def main():
    
    temp_tag = TemporalTagger()
    '''
    temp_tag.temporal_tagger("1986-1987")
    temp_tag.temporal_tagger("11/1986-11/1987")
    temp_tag.temporal_tagger("11/19-11/19")
    temp_tag.temporal_tagger("98/09-19/09")
    temp_tag.temporal_tagger("1992.9-1993.8")
    temp_tag.temporal_tagger("1992.9\xe21993.8")
    temp_tag.temporal_tagger("1992.9 \xe2 1993.8")
    temp_tag.temporal_tagger("1986-87")
    temp_tag.temporal_tagger("1986-1987")
    temp_tag.temporal_tagger("nsdnmsd 09.1986 - 09.1986 skdjskj")
    temp_tag.temporal_tagger("sept 1987 - sept 1986")
    temp_tag.temporal_tagger("september 1987 - september 1986")
    temp_tag.temporal_tagger("sept.1987-sept.1986")
    temp_tag.temporal_tagger("sept 1987 -")
    temp_tag.temporal_tagger("sept.1987-")
    temp_tag.temporal_tagger("sept.1987 ")
    temp_tag.temporal_tagger("2010")
    temp_tag.temporal_tagger("7/1987 ")
    temp_tag.temporal_tagger("7.1987 ")
    temp_tag.temporal_tagger("7-1987 ")
    temp_tag.temporal_tagger("07.87 - 09.99")
    temp_tag.temporal_tagger("Oct. 21 - 24")
    temp_tag.temporal_tagger("october 1985 to july 1991")
    temp_tag.temporal_tagger(" sep. 2009 ")
    
    temp_tag.temporal_tagger("february 1982 february 1984")
    temp_tag.temporal_tagger("Research Assistant Professor     Purdue University                              May 2005       July 2007")
    temp_tag.temporal_tagger("july   2005 -")
    temp_tag.temporal_tagger('may 2005       july 2007')
    temp_tag.temporal_tagger('september 1999 – june 2005')
    temp_tag.temporal_tagger('1967 \xe2 1989')
    '''
    print temp_tag.temporal_tagger('1967 1989').duration_string()
    print temp_tag.temporal_tagger('August 1997 - January 2012').duration_string()
    print temp_tag.temporal_tagger("september 1987 ~ september 1986").duration_string()
if __name__ == "__main__":
    main()