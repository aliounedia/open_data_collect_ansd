import urllib, re, os, sys
datadir   = "datas"
originale = "http://www.ansd.sn/"

# Match an Html link page 
regex     = re.compile("""\s*(?i)href\s*=\s*
                (
                \"([^\"]*\")|
                  '[^']*'|
                  ([^'\">\s]+)
                )""" , re.MULTILINE | re.VERBOSE)

def find_link(url, type):
    """
    Find An Html Link Page , iterate over link page and return
    link if it end with a given type.
    """
    url    = urllib.urlopen(url)
    buffer = url.read()
    for html_link  in regex.finditer(buffer):
        link_part = html_link.group(1).strip('"')
        if  link_part.endswith(type):
            yield link_part

def grab_file(fisrt_turl, type):
    """
    Download file with given type 
    """ 
    for item  in  find_link(fisrt_url,type):
        # Build The next url by adding The Original url to
        # the item/Link .There is no link with The  Hml Page
        # where we are and the link that it contain 
        next_url = originale + item
        if next_url.endswith(type):
             # Donload file
             download_file(next_url, type)

def grab_file_link(fisrt_url, type):
    """
    Download file with given type 
    """ 
    for item  in  find_link(fisrt_url,type):
        # Build The next url by adding The Original url to
        # the item/Link .There is no link with The  Hml Page
        # where we are and the link that it contain 
        next_url = originale + item
        if next_url.endswith(type):
             # Donload file
            open( 'test.txt',  'a') .write(
                 '-'*40 + '\n'    + 
                 next_url +  "\n" +
                 fisrt_url +  "\n" + 
                  '-'*40 + '\n')
       
def find_html_link(url_page):
    """
    use  the "find_link" to  get all html links into the given page
    """
    for htm_page in find_link(url_page, "html"):
        # To get the next page I Add The originale to the item
        htm_page1 = originale + htm_page
        print >> sys.stdout , "htm_page " , htm_page
        yield  htm_page1
        find_html_link(htm_page)



def  find_link_recurse(url_page, seen =set()):
     """ Fin a link recursively , if the url is already in seen
     skeep it and go to the next url """
     for url_page  in find_link(url_page, 'html'):
         if url_page not in seen:
                seen.append(url_page)
     


def  download_file(url , type):
     """
     Download the Html Page 
     """
     response = urllib.urlopen(url)
     name   = url.replace("|", "_")
     name   = name.replace("/" , "_")
     name   = name.replace("\\" , "_")
     name   = name.replace("http:" , "")
     buffer = response.read()
     name   = "datas\%s%s" % (name, type)
     if os.path.exists(name):
         return 
     with open(name, "wb") as  fs:
         fs.write(buffer)
        
if __name__== "__main__":
    for url in  find_html_link('http://www.ansd.sn/produist_et_services.html'):
        print grab_file_link(url, '.pdf')

    
