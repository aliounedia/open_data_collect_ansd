import ckanclient
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
            'url': "https://commondatastorage.googleapis.com/ckannet-storage/2011-11-24T112025/AfTerFibre_21nov2011.csv",
            'download_url': "https://commondatastorage.googleapis.com/ckannet-storage/2011-11-24T112025/AfTerFibre_21nov2011.csv",
            'tags': "Senegal ANSD",
            "groups" :['country-sn'],
            'notes': "Senegal ANSD  donnees",
        }
        sn = self.group_entity_get("country-sn")
        
        self.package_register_post(package_entity)
##        self.add_package_resource('test_python_client_package',
##        'https://commondatastorage.googleapis.com/ckannet-storage/2011-11-24T112025/AfTerFibre_21nov2011.csv',
##            name='Foo', resource_type='metadata', format='csv')
    
if __name__ == '__main__':
    # http://thedatahub.org/api/rest/package
    # http://datahub.io/group/country-sn
    ckan_post  = CkanPost("http://datahub.io/api",
        "a3c845db-f5f8-44af-a493-5ca5f6eccd93",
        True,
        "aliounedia",
        "aliounedia")
    print 'ckan isntance', ckan_post
    ckan_post.test_post_package_resource()
           
           


         



          
          
