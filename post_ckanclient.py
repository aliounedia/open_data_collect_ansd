# -*- coding: latin-1 -*-
import ckanclient, sys, codecs,re
from utils.datasets import ansd_dataset
data_link_desc = "datas/descriptions"

class CkanPost(ckanclient.CkanClient):
    def __init__(self, base_location=None, api_key=None, is_verbose=False,
                 http_user=None, http_pass=None, **kwargs):
        ckanclient.CkanClient.__init__(
           self, 
           base_location = base_location,
           api_key=api_key,
           is_verbose = is_verbose,
            http_user = http_user,
           http_pass  = http_pass)

    def test_post_package_resource(self):
        """
        help Me to test upload ressource to Ckan server
        """
        package_entity = {
            'name': 'ansd_statistiques_sur_les_menages',
            'url': "https://commondatastorage.googleapis.comckannet-storage/2011-11-24T112025/AfTerFibre_21nov2011.csv",
            'download_url': "https://commondatastorage.googleapis.comckannet-storage/2011-11-24T112025/AfTerFibre_21nov2011.csv",
            'tags': "Senegal ANSD",
            "groups" :['country-sn'],
            'notes': "Senegal ANSD  donnees",
        }
        self.package_register_post(package_entity)

    def post_package_resource(self , dict):
        """
        Method to add package ressource to datahub
        """
        self.package_register_post(dict)

    def serve_forever(self):
        """

        Like a server , this method will  check all datasetx
        to update  from all dataset link (datas/links/links)
        and there corresponding  descriptions from (
        datas/descriptions, and will update
        to http://datahub.io/api
        
        """
        while True:
           
            try:
                for link  in link_finder():
                  dict = {}
                  try:
                    file_desc  = file_from_link(link)
                  except:
                      print sys.stdout >> \
                        'No descpription for this link ', file_desc
                      continue
                  else:
                      # get the description of the dataset
                      # from file.
                      desc  = ""
                      try:
                         desc =  codecs.open("%s/%s" % (
                                 data_link_desc,  file_desc) ,
                                    'rb' , encoding= "latin-1").read()
                      except Exception, e:
                        print e
                        continue
                        print  >> sys.stdout, "Cannot read file descrption \n %s/%s"\
                              % (data_link_desc,file_desc)
                        continue
                      else:
                           # create  the ckan package identity
                           dict['name']         = file_desc.lower().replace(".", "_").\
                                replace("-", "_").replace(" ", "_")
                           dict['download_url'] = clean_crlf(link)
                           dict['url']          = clean_crlf(link)
                           dict['tags']         =\
                                "Senegal ANSD donnees menages publications"
                           dict["groups"]       = ['country-sn']
                           dict['notes']        = desc
                           # ok, try to post data set
                           if dict['name'] in ansd_dataset():
                               print  >> sys.stdout, "This name is already saved"
                               continue
                           try:
                               self.package_register_post(dict)
                               print 'ok'
                           except Exception ,e :
                               print e
                               print dict
                               continue
                               print  >> sys.stdout,\
                               "cannot update dataset ",\
                                     link           
            except Exception , e:
                print e

def clean_crlf(str):
    return re.sub("[\r|\n|\n\r]" , "" , str)

def file_from_link(link):
    """
    Generate a filename from link name
    """
    return link.replace("|", "_").replace("/", "_").\
           replace("\\", "_").replace("http:" , "").\
           replace("\n", "").replace("\r", "") + ".txt"

def link_finder(data_link_path = "datas/links/link.txt"):
    """
    Irate over links
    """
    with open(data_link_path, "rb") as data_link_file:
        links  = data_link_file.readlines()
        for link in links :
            yield link 

if __name__ == '__main__':
    # http://thedatahub.org/api/rest/package
    # http://datahub.io/group/country-sn
    ckan_post  = CkanPost("http://datahub.io/api",
        "b3c845db-f5f8-44af-a493-5ca5f6eccd94",
        True,
        "xxx",
        "xxx")
    print 'ckan isntance', ckan_post
    #ckan_post.test_post_package_resource()
    ckan_post.serve_forever()
           
           


         



          
          
