'''
Created on Sep 3, 2014

@author: subhash
'''

class FilterDataset:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.filename = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/work_section/work_desig_list.txt"
        self.token = dict()
        self.max_cnt = 0

    def filter_dataset(self):
        
        for line in open(self.filename):
            line = line.replace("\n", "")
            
            tokens = line.split(" ")
            
            tokens_len = len(tokens)
            
            if tokens_len > self.max_cnt:
                self.max_cnt = tokens_len
                
            if tokens_len not in self.token:
                self.token[tokens_len] = list()
                
            self.token[tokens_len].append(line)

        

def main():
                
    filt_data = FilterDataset()
    filt_data.filter_dataset()
    fileW = open("/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/work_section/work_desig_filt.txt", "w")
    for cnt in range(filt_data.max_cnt + 1):
        
        index = filt_data.max_cnt - cnt
        print index
        
        if index in filt_data.token:
            tokens = filt_data.token[index]
            for item in tokens:
                fileW.write(item + "\n")
        
if __name__ == "__main__":
    main()