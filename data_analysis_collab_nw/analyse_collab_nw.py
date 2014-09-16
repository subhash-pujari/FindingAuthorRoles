'''
Created on Aug 29, 2014

@author: subhash
'''


class Analyse_Collab_NW:
    
    def __init__(self):
        self.path = "/home/subhash/Dropbox/master_major_project/dataset/"
        self.inproc = "inproceedings.tsv"
        self.pub_info = dict()
        self.auth_info = dict()
        pass

    def initialise_pub(self):
        for line in open(self.path + self.inproc):
            line = line.replace("\n", "")
            tokens = line.split("\t")
            year = tokens[0]
            conf = tokens[1]
    
    def initialise_auth(self): 
        pass


def main():
    
    ana_collab = Analyse_Collab_NW()
    ana_collab.initialise_pub()
    pass
    
if __name__ == "__main__":
    main()