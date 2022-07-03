# coding=utf-8
import sys
import os
import glob
import bs4
import pprint
import json
import re



arrayword={}
arrayhtml=[]

nbword = 0
nbdocument = 0

stopword = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def splitwordinlist( lst ):
    result = []
    for w in lst:
        lsplit = re.split('[\{\}\*\[\]=\'\"\(\)_\-\\\\/,;.:+#!?]', w)
        for r in lsplit:
            if len(r) == 0:
                continue
            # NO NUMBER ...
            if r.isnumeric() is False:
               result.append(r)
    return result

def create_test_index():
    global arrayword
    global arrayhtml
    global nbword
    global nbdocument
    n= 0 
    files = glob.glob("html/*" )
    for f in files :
          #if n > 10 : 
          #    break
          if (os.path.isdir(f)) :
              fullpath="%s/%s.html" % ( f,f.replace("html/","") )
              print(fullpath)
              nbdocument = nbdocument + 1

              with open(fullpath, 'r') as f:
                    webpage = f.read()


                    soup = bs4.BeautifulSoup(webpage,features="lxml")
                    txt=soup.get_text()
                    lstw = splitwordinlist(txt.split())
                    for w in lstw:

                        w = str(w).lower()
                        if w in stopword:
                            continue
                        # no word less 3 caracter.
                        if len(w) < 3: 
                            continue

                        if len(w) > 3: 
                           # no word alphanumeric.
                           if re.match("[a-zA-Z0-9]*[0-9]+[a-zA-Z]+",w) :
                               continue
                           if re.match("[a-zA-Z0-9]*[0-9]+",w) :
                               continue

                        if w not in arrayword:
                            nbword = nbword + 1
                            arrayword[w]={}
                            arrayword[w][n] = 1
                        else:
                            if n not in arrayword[w]:
                                arrayword[w][n] = 1
                            else:
                                arrayword[w][n] =  arrayword[w][n] + 1

              arrayhtml.append(fullpath)
              n=n+1


if __name__ == '__main__':
    create_test_index()
    with open('json_data.json', 'w') as outfile:
        json.dump({"files": arrayhtml,"word":arrayword,"nbword":nbword,"nbdocument":nbdocument},outfile,indent=4)
