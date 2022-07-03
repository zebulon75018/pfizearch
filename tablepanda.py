import pandas as pd
import sys
import glob
import os
import pprint
 
files = glob.glob("html/*" )
for f in files :
          if (os.path.isdir(f)) :
              fullpath="%s/%s.html" % ( f,f.replace("html/","") )
              print(fullpath)
              try :
                 df_list = pd.read_html(fullpath) 
                 df.to_csv(fullpath.replace(".html",".csv"))
                 print(len(df_list))
              except Exception as e :
                  pass

