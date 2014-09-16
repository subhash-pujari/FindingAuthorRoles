'''
Created on Sep 12, 2014

@author: subhash
'''
import random
from scrap_education import ScrapEducation
from scrap_work import ScrapWork
from util import file_interface
import datamodel

def main():
    path = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/pdfToText2.0/"
    path_output = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/"
    path_filt_res = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/resume_filter/"
    
    scrap_edu = ScrapEducation()
    scrap_work = ScrapWork()
    fileW_edu = open(path_output + "education_section.txt", "w")
    fileW_work = open(path_output + "work_section.txt", "w")
    file_int = file_interface.FileInterface()
    file_list = file_int.get_file_list(path)
    
    fileW_both_sec = open(path_output + "resume_both_sec.tsv")
    
    count = set()
    count_work = 0
    count_edu = 0
    
    count_both_sec = 0
    file_list = list()
    for line in fileW_both_sec:
        line = line.replace("\n", "")
        file_list.append(line)
    
    print len(file_list)
    
    '''
    random_file_list = list()
    while len(random_file_list) < 6:
        index = random.randint(0, len(file_list)-1)
        random_file_list.append(file_list[index])
    
    #random_file_list = ['3713_0.txt']
    '''
    
    random_file_list = file_list
    iden_res = set()
    
    for index in range(len(random_file_list)):
        
        
        filename = random_file_list[index]
        print filename
        resume = datamodel.Resume(path + filename)
    
        identified_sections = list()
        for section in resume.section_list:
            if section.start < 150 and (section.end - section.start) < 70 and section.sec_type == "work":
                section = scrap_edu.scrap_edu(section, filename)
                identified_sections.append(section)
                
            if section.start < 100 and (section.end - section.start) < 50 and section.sec_type == "education":
                section = scrap_edu.scrap_edu(section, filename)
                identified_sections.append(section)
        
        edu_flag = False
        work_flag = False
        
        for section in identified_sections:
            if section.sec_type == "education":
                edu_flag = True
            elif section.sec_type == "work":
                work_flag = True
                
        if edu_flag and work_flag:
            tokens = filename.split("_")
            _id = tokens[0]
            iden_res.add(_id)
            
        timeline_list = convert_tags_to_timeline(identified_sections)
        timeline_list = sort_time_line(timeline_list)
        print_timeline(timeline_list)
        
        fileW_res_filt = open(path_filt_res + filename, "w")
        
        for item in timeline_list:
            
            temp = item[0]
            deg_desig = item[1]
            print temp
            print deg_desig
            fileW_res_filt.write(temp.duration_string() + "\t" + deg_desig[0] + "\n")
            
    '''
    fileW_iden_res = open(path_output + "iden_res.txt", "w")
    for _id in iden_res:
        fileW_iden_res.write(_id + "\n")
    '''
             
def print_timeline(timeline_list):
    
    for index in range(len(timeline_list)):
        item = timeline_list[index]
        print index
        print item[0].duration_string()
        print item[1]
        
def comp(item1, item2):
    
    
    if item1[0].start_date.year >= item2[0].start_date.year:
            return True
    else:
        return False
    
def sort_time_line(itemlist):

    
    for i in range(len(itemlist)):
        max_item = itemlist[i]
        index = 0
        for j in range(i, len(itemlist)):
            if comp(itemlist[j], max_item):
                max_item = itemlist[j]
                index = j
        
        itemlist[index] = itemlist[i]        
        itemlist[i] = max_item

    return itemlist
            
            
        

def create_tag_map(line_list):
    
        tag_map = [[False for x in xrange(3)] for x in xrange(len(line_list))]
        
        # create tag map for each line to indicate whether the temporal degree and designation tags are present or not
        for index in range(len(line_list)):
                
                
            line = line_list[index]
                
                # make true for all the tags that are present
            if len(line.temporal_tags) > 0:
                tag_map[index][0] = True
            if len(line.degree_tags) > 0:
                tag_map[index][1] = True
            if len(line.desig_tags) > 0:
                tag_map[index][2] = True
        
        
        return tag_map

def create_relation(line, prev_line, tag_list, prev_tag_list):
    pass

def convert_tags_to_timeline(section_list):
        
        
        
        timeline_list = list()
        for section in section_list:
                
            line_list = section.line_list
            

            tag_map = create_tag_map(line_list)

            
            # we check for all the lines to map the tags that are present in the section
            for index in range(len(tag_map)):
                
                              
                
                # get list of all tags in the list
                tag_list = tag_map[index]
                line = line_list[index]
                
                if index > 0:
                    prev_tag_list = tag_map[index-1]
                    prev_line = line_list[index-1]
                
                
                temp_tag = None
                deg_tag = None
                desig_tag = None
                deg_desig = None
                
                
                # both the degree and desination tag are present chose one of them
                if tag_list[1] and tag_list[2]:
                    deg_desig = line.desig_tags
                    desig_tag = line.desig_tags
                    deg_tag = None
                    # when you chose one of them make the other one False as there can not be degree and designation tags in the same line in principle
                    tag_map[index][1] = False
                    
                # only degree tag is present
                elif tag_list[1]:
                    deg_desig = line.degree_tags
                    deg_tag = line.degree_tags
                    desig_tag = None
                    
                # only designation tag is present
                elif tag_list[2]:
                    deg_desig = line.desig_tags
                    deg_tag = None
                    desig_tag = line.desig_tags
                
                if deg_desig is not None:
                    print deg_desig
                
                # all the tags in the given line are satified in this case
                # temporal tag and either of degree or designation tag is there
                if tag_list[0] and deg_desig is not None:
                    pass
                    print "both present start>>"
                    print line.temporal_tags[0].duration_string()
                    print deg_desig
                    print "both present end>>"
                    
                    temp_tag = line.temporal_tags[0]
                    
                    # make all as false
                    tag_map[index][0] = tag_map[index][1] = tag_map[index][2] = False
                    
                # unsatisfied temporal tag 
                elif tag_list[0]:
                    # check_for_unsatisified degree or designation tag in previous line
                    
                    # if first line just continue
                    if index == 0:
                        continue
                    
                    
                    # get the tags from the previous line
                    prev_tag_list = tag_map[index-1]
                    prev_line = line_list[index-1]
                    
                    # if a temporal tag is present in the previous line. No need to go further
                    if prev_tag_list[0]:
                        continue
                                        
                    # if degree tag is there
                    elif prev_tag_list[1]:
                        print "temporal present start>>"
                        print line.temporal_tags[0].duration_string()
                        print prev_line.degree_tags
                        print "temporal present end>>"
                        
                        temp_tag = line.temporal_tags[0]
                        deg_tag = prev_line.degree_tags
                        desig_tag = None
                        
                        tag_map[index][0] = False
                        tag_map[index-1][1] = False
                        
                    # if desig tag is there
                    elif prev_tag_list[2]:
                        print "temporal present start>>"
                        print line.temporal_tags[0].duration_string()
                        print prev_line.desig_tags
                        print "temporal present end>>"
                        
                        temp_tag = line.temporal_tags[0]
                        deg_tag = None
                        desig_tag = prev_line.desig_tags
                        
                        tag_map[index][0] = False
                        tag_map[index-1][2] = False
                        
                #unsatisfied degree or desig tag
                elif deg_desig is not None:
                    
                    if index == 0:
                        continue
                    
                    # get the tags from the previous line
                    prev_line_tags = tag_map[index-1]
                    prev_line = line_list[index-1]
                    
                    # in prevous line temporal tag is present but none of degree and designation tags are present in the previous line
                    if prev_line_tags[0] and not (prev_line_tags[1] or prev_line_tags[2]):
                        print "degree_desig present start>>"
                        print prev_line.temporal_tags[0].duration_string()
                        print deg_desig
                        print "degree_desig present end>>"
                        tag_map[index-1][0] = False
                        tag_map[index][1] = False
                        
                        temp_tag = prev_line.temporal_tags[0]
                    
                
                # none of the tags are present    
                else:
                    pass
                    
                if temp_tag is not None and (deg_tag is not None or desig_tag is not None):
                    
                    print "details of time line item >> start >>"
                    print temp_tag.duration_string()
                    if deg_tag is not None:
                        print deg_tag
                        timeline_list.append((temp_tag, deg_tag))
                    elif desig_tag is not None:
                        print desig_tag
                        timeline_list.append((temp_tag, desig_tag))
                    print "details of time line item >> ends >>"   
                    
        return timeline_list
    
    
if __name__ == "__main__":
    main()