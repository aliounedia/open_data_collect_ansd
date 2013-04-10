from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
#codec = 'utf-8'
codec = 'latin-1'
laparams = LAParams()
caching = True
imagewriter = None
pagenos = set()
password = ""
import StringIO , sys
class FileWrapper:
    """ A simple File Wrapper class to get file descprion """
    def __init__(self, stream):
        self.stream = stream
        
    def get_description(self):
        try: 
            return self.stream[:500]
        except:
            return  self.stream
   
class FileConverter:
    def __init__(self, file_name):
        """
        check that name of the file add call the converter class
        that match. the result should be a text file, for this moment
        handle juste an pdf file and raise error if this happen.
        """
        self.file_name = file_name
        if not self.file_name.endswith('.pdf'):
            raise ValueError("Give an  pdf file please , the converter"\
                    "does not handle others files")
                             
    def convert_file(self):
        """ Convert file to Text """                     
        rsrcmgr = PDFResourceManager(caching=caching)
        outfp =  StringIO.StringIO()             
        device = TextConverter(
            rsrcmgr, outfp, codec=codec, laparams=laparams,
                               imagewriter=imagewriter)

        fp = file(self.file_name, 'rb')
        print >> sys.stdout, fp.read()[:20]
        
        process_pdf(rsrcmgr, device, fp, pagenos,
                    maxpages=1, password=password,
                    caching=caching, check_extractable=True)

        fp.close()
        device.close()
        value = outfp.getvalue()
        outfp.close()
        return FileWrapper(value)

if __name__ == "__main__":
     """
     Output should be CATALOGUE  DES RESSOURCES
     DINFORMATION DE LANSD

     JUIN 2006
     """
     wrapper =FileConverter(
        '__www.ansd.sn_publications_catalogue.pdf').\
                convert_file()
     print >> sys.stdout, "File cotent ", wrapper.get_description()
        
        
