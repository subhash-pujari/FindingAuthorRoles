from os import listdir
from os.path import isfile, join

import MySQLdb
import re

def main():
    path = "/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/pdfToText2.0/" 

    files = [ f for f in listdir(path) if isfile(join(path,f)) ]
    
    author_id_list = list()
    
    for filename in files:
        
        tokens = filename.split("_")
        author_name = tokens[0]
        author_id_list.append(author_name)

    
    print len(author_id_list)

    db = MySQLdb.connect('localhost', 'tiger', 'user@123', 'authRole')
    cursor = db.cursor()
    count = 0
    
    fileW = open("/home/subhash/Dropbox/master_thesis/code_role_determiner1.1/dataset/author_disambigouous.txt", "w")
    
    id_set = set()
    for _id in author_id_list:
        sql = "select author1 from auth_hp where id ="+_id+" and author2 is NULL;"
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data)>0:
            name = data[0][0]
            if len(re.findall("[0-9]", name)) == 0:
                print name
                fileW.write(_id + "\t" + name + "\n")
                count = count + 1
                id_set.add(_id)
                
                    
    print count
    print len(id_set)
        
    

if __name__ == "__main__":
    main()