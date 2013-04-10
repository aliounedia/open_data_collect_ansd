#! /usr/bin/env python 
# This file try to build the descption  for a dataset that point 
# to some file .When whe create a dataset that point to some file
# like a pdf whe need to read some datas from it , just the first
# page , to help someone got some information about this dataset
# because , in some dataset hubs like ckan , people chech first
# the dataset descprition to know about.

from file_converter import FileConverter
import sys , urllib , os, re
data_link_desc = "datas/descriptions"

# If you need to create file decption for others file
# types ,juste add this type here .For this instant
#  I handle juste a Pdf file.

valide_extensions = ["pdf"]

def _description(data_link_path = "datas/links/link.txt"):
    """
    Build the  file descpription :
    1 - For each link into the file ,try to dowload it
    2 - Retreive  500  firsts line form firt page
    3 - create a file with the same name of the current link and
        by replacing (/ to _) (\ to _) , ( " " to _) , because
        filename does not accept some carrecteres from link
    4 - Remove the file dowloaded
    """
    if not os.path.exists(data_link_desc):
        os.mkdir(data_link_desc)
                
    with open(data_link_path, "rb") as data_link_file:
        links  = data_link_file.readlines()
        for link in links:
            # check if this file is valide , ie his extension is
            # into valide_extensions
            try:
                ext = link.split(".")[-1].strip()
            except:
                print >> sys.stdout, "This link is not a valide link %s" % link
                #return 
            print >> sys.stdout, "The file extension ", ext.lower()
            if not ext.lower() in valide_extensions:
                print >> sys.stdout, "This is not a valide extension"
                #return
                continue
            # get the pdf file_name that match the given link
            try:
                download(link)
            except:
                print >> sys.stdout , 'Error to download link %s' % link
                #raise 
                continue
            link_file =  file_from_link(link) + ".pdf"
            print link_file
            # Get the converter
            converter = FileConverter(
                   "%s/%s" % (data_link_desc, link_file))
            
            try:
                converted   = converter.convert_file()
            except:
                print >> sys.stdout, 'Error converting datas'
                #raise 
                continue
            # :) Ya I got a descprition
            description = converted.get_description()
            description = clean_description(description)
            # writing data into the file description
            link_file =  file_from_link(link) + ".txt"
            if os.path.exists("%s/%s" %(data_link_desc, link_file)):
                print >> sys.stdout , 'The descrition already exits'
                continue
            with open("%s/%s" %(data_link_desc, link_file), "wb") as fs:
                 fs.write(description)

def clean_description(description):
    """
    clean description and return a more human readable
    descrpiption
    """
    return re.sub("[\r|\t|\r\n|\.*|\-*]", "", description) 
    
def file_from_link(link):
    """
    Generate a filename from link name
    """
    return link.replace("|", "_").replace("/", "_").\
           replace("\\", "_").replace("http:" , "").\
           replace("\n", "").replace("\r", "")

def download(link):
    """
    Download link 
    """
    buffer  = urllib.urlopen(link).read()
    link    = file_from_link(link) + ".pdf"
    if os.path.exists(link):
         return
        
    with open("%s/%s" %(data_link_desc, link), "wb") as fs:
         fs.write(buffer)

if __name__ == "__main__":
  _description() 
