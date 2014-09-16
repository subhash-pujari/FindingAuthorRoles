class TemporalTags:
    
    def __init__(self, temp_str_list, str_type, dur_sep, month_year_sep, is_month_year, is_year_4, is_month_num):
    
        self.temp_str_list = temp_str_list
        self.str_type = str_type
        self.dur_sep = dur_sep
        self.month_year_sep = month_year_sep
        self.is_month_year = is_month_year
        self.is_year_4 = is_year_4
        self.is_month_num = is_month_num


class DurationExtraction:
    '''
    The duration extractor takes different type of temporal tags.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.month_num = {1:1, 2:1, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12}
        self.month_str_short = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6 ,'june':6, 'jul':7,'july':7, 'aug':8, 'sept':9, 'sep':9, 'oct':10, 'nov':11, 'dec':12}
        self.month_str_long = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6, 'july':7, 'august':8, 'september':9, 'october':10, 'november':11, 'december':12}
    
    def get_month_num(self, month):
        
        month = month.strip()
        
        if int(month) in self.month_num:
            month = self.month_num[int(month)] 
        else:
            month = None
            
        return month
    
    def get_month_str(self, month):
        
        month = month.strip()
        
        if month in self.month_str_short:
            month = self.month_str_short[month] 
        elif month in self.month_str_long:
            month = self.month_str_long[month]
        else:
            month = None
            
        return month
    
    def get_month(self, month, is_month_num):
        if is_month_num:
            month = self.get_month_num(month)
        else:
            month = self.get_month_str(month)
            
        return month
    
    def get_date_(self, month, year, is_year_4, is_month_num):
        year = year.strip()
        
        if is_year_4:
            year = int(year)
        else:
            # convert year from length 2 to length 4
            if int(year) < 15:
                year = '20' + year
            else:
                year = '19' + year
                
        month = self.get_month(month, is_month_num)
        date = DateTime(None, month, int(year))
        return date
    
    def get_date(self, date_string, sep, is_month_year, is_month_num, is_year_4):
        
        # remove the escape character added for reg exp
        if len(sep) > 1:
            sep = sep.replace('\\', '')
            
        date_string = date_string.strip()
        date_tokens = date_string.split(sep)
        if is_month_year:
            month = date_tokens[0].strip()
            year = date_tokens[1].strip()
        else:
            month = date_tokens[1].strip()
            year = date_tokens[0].strip()
        
        return self.get_date_(month, year, is_year_4, is_month_num)
            
    def remove(self, token, str_list):
        while token in str_list:
            str_list.remove(str)

        return str_list
    
    def duration_extraction(self, temporal_tags):
        # temp_str_list, str_type, dur_sep, month_year_sep, is_month_year, is_year_4, is_month_num
        tag_list = temporal_tags.temp_str_list
        #print tag_list
        if temporal_tags.str_type is 'full':
            for tag_string in tag_list:
                if type(tag_string) is tuple:
                    tag_string = tag_string[0]
                    
                tag_string_token = tag_string.split(temporal_tags.dur_sep)
                
                if temporal_tags.dur_sep == temporal_tags.month_year_sep:
        
                    #self.remove(self, '', temporal_tags)
                    if len(tag_string_token) == 4:
                        start = tag_string_token[0] + temporal_tags.month_year_sep + tag_string_token[1]
                        end = tag_string_token[2] + temporal_tags.month_year_sep + tag_string_token[3]
                else:
                    start = tag_string_token[0]
                    end = tag_string_token[1]
                        
                start = self.get_date(start, temporal_tags.month_year_sep, temporal_tags.is_month_year, temporal_tags.is_month_num, temporal_tags.is_year_4)
                end = self.get_date(end, temporal_tags.month_year_sep, temporal_tags.is_month_year, temporal_tags.is_month_num, temporal_tags.is_year_4)
                           
        elif temporal_tags.str_type is 'half':
            for tag_string in tag_list:
                
                
                if type(tag_string) is tuple:
                    tag_string = tag_string[0]
                    
                if temporal_tags.dur_sep is " ":    
                    if temporal_tags.month_year_sep is not " ":
                        tag_string = tag_string.replace(" ", "")              
                
                tag_string = tag_string.split(temporal_tags.dur_sep)
                
                # this if is in case of where dur and month year sep are same
                if temporal_tags.dur_sep == temporal_tags.month_year_sep:
                    tag_string = tag_string[0] + temporal_tags.month_year_sep + tag_string[1]
                else:
                    tag_string = tag_string[0]

                tag_string = tag_string.strip()
                start = tag_string
                start = self.get_date(start, temporal_tags.month_year_sep, temporal_tags.is_month_year, temporal_tags.is_month_num, temporal_tags.is_year_4)
                end = None
                
        elif temporal_tags.str_type is 'year':
            for tag_string in tag_list:
                year = tag_string.strip()
                start = DateTime(None, None, int(year))
                end = None
                
        elif temporal_tags.str_type is 'year_duration':
            for tag_string in tag_list:
                tokens = tag_string.split(temporal_tags.dur_sep)
                start = tokens[0].strip()
                start = DateTime(None, None, int(start))
                end = tokens[1].strip()
                end = DateTime(None, None, int(end))
        
        duration = Duration(start, end) 
        return duration
        
        
class DateTime:
    
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def date_string(self):
        
        line = ""
        if self.day is not None:
            line = line + self.day + "\t"
        
        if self.month is not None:
            line = line + str(self.month) + "\t"
            
        if self.year is not None:
            line = line + str(self.year) + "\t"
            
        return line
    
class Duration:
    
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        
    def duration_string(self):
        
        line = ""
        if self.start_date is not None:
            line = line + self.start_date.date_string() + "\t"
        
        if self.end_date is not None:
            line = line + self.end_date.date_string() + "\t"
 
        return line
        