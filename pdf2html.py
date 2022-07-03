import sys
import os
import glob



if __name__ == '__main__':
      files = glob.glob("*.pdf" )
      for f in files :
              print( f )
              os.system("pdftohtml -p -s -stdout  %s > html/%s " % (f, f.replace(".pdf",".html")))

