import sys
import os
import glob



if __name__ == '__main__':
      files = glob.glob("*.csv" )
      for f in files :
              print( f )
              os.system("python csvstathtml.py --json  \"%s\" >  \"%s\" " % (f, f.replace(".csv",".json")))

