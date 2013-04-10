# The file allow you to parse a site links recursively and put
# all links  that match the given pattern into the link_output.txt
# file , for if you give them http://datahub.com for exemple , il
# and extension =".pdf", il will  retreive all pdf file link into
# the ink_output.txt

import urllib, re, os
# Match an Html link page 
regex  = re.compile("""\s*(?i)href\s*=\s*
                (
                \"([^\"]*\")|
                  '[^']*'|
                  ([^'\">\s]+)
                )""" , re.MULTILINE | re.VERBOSE)

original  = "http://www.ansd.sn/"
output    = "datas/links"
seen      = set()
def _link_parser(url, extension, top_level=False):
    """
    url is the first url name that take our link_parser.
    extension is the extension of the the file , that match our
    link
    """
    url  = urllib.urlopen(url)
   
    # Check if url is already is seen, if not go and recurse
    # to extract all links that are into the  - url page
    buffer = url.read()
    for html_link in regex.finditer(buffer):
        link  = html_link.group(1)
        link  = link.strip('"')
        #link  = link.strip("'")
        #link  = link.lower()
        # if top_level =true , so append to the link the orginal url
        if top_level:
            link  = "%s%s" % (original, link)
        # if the link end with hmtl , recurse on it and
        # retreive all links
        if  link.endswith(".html") and link not in seen:
            seen.add(link)
            _link_parser(link, extension, top_level)

        if not os.path.exists(output):
                os.mkdir(output)
                
        # if the link  match the extension, so add it to the list
        # of links
        print link
        if link.endswith(extension) and not infile(link):
            open( "%s/%s" %(output, "link.txt"),
                  "a").write("%s\n" % link)
    print 'Ok'

def infile(link):
    """
    Verify if this link is not already in datas/link.txt , to prevent
    line duplication.
    """
    links = []
    try:
        links =  open( "%s/%s" %(output, "link.txt") , "rb")\
                .readlines()
    except IOError,e:
        pass
    if link in links:
        return True
    return False

if __name__ == '__main__':
   _link_parser("http://www.ansd.sn" , "pdf" , True)

