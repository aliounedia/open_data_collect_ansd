# -*- coding: latin-1 -*-
import ckanclient, sys, codecs,re
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

    def ansd_dataset(self):
        """ return the set of datasets for ansd """
        i = 0
        list =[]
        for package in  self.package_list():
            if re.match("__www_ansd", package):
                list.append(package)
        return list

    def ansd_updated_dateset(self):
        """return the list of upated datasets of ansd
	it check  the content of - ansd_uopdated.text-
	wich contain the datasets renamed by the team
       (This file is sotored to google drive , I made
	regulary an update)
        """
        def ():  
             with open("ansd_updated.text", "rb") as f:
                 return map(lambda line: line.strip(),
                            f.readlines())


        try:
            return get_datasets():
        except:
            # We return 0 here to tell update_ckan.py
            # when it run serve_forver to not update
            # to ckan datahub
            return 0
        
    def __repr__(self):
        """ return the set of datasets for ckan """
        i = 0
        for package in  self.package_list():
                print package
                i +=1
        print 'len :', i

ckan_post  = CkanPost("http://datahub.io/api",
        "a3c845db-f5f8-44af-a493-5ca5f6eccd93",
        True,
        "aliounedia",
        "aliounedia")

ansd_dataset     =     ckan_post.ansd_dataset
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
    ckan_post.__repr__()
           
           


         



          
          
